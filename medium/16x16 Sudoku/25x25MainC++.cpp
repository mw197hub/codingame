#include <cstdlib>
#include <cstdio>
#include <cstdint>
#include <cstring>
#include <cassert>
#include <random>
#include <chrono>
#include <algorithm>


#define N       5
#define N_2     (N*N)
#define base    'A'
#define vide    '.'

char solution[N_2][N_2+1] = {0};

typedef union
{
    uint16_t size;  // for headers
	uint16_t head;	// for cells
} dlx_t;

typedef struct _node
{
	dlx_t data;
    uint16_t left;
    uint16_t right;
    uint16_t up;
    uint16_t down;
} Node;


static Node pool[1+4*N_2*N_2+4*N_2*N_2*N_2];
Node * root_    = &pool[0];
Node * headers_ = &pool[1];
Node * nodes_   = &pool[1+4*N_2*N_2];  // pool of nodes


void InitRoot (Node* root)
{
    root->left = root->right = 0;
}

void InitNode (Node* header, Node* last, Node* node)
{
    const uint16_t hidx = header - root_;
    const uint16_t lidx = last - root_;
    const uint16_t idx  = node - root_;

    // gestion des liens up & down
    node->data.head = hidx;
    node->down = hidx;
    node->up = header->up;
    pool[header->up].down = idx;
    header->up = idx;

    // gestion des liens right & left
    if (last == NULL)
    {
        node->left = node->right = idx;
    }
    else
    {
        node->left = lidx;
        node->right = last->right;
        pool[last->right].left = idx;
        last->right = idx;
    }
    // incremente nbElements du header
    header->data.size++;
}

void cover (Node* header)
{
    // supprime le header
    pool[header->left].right = header->right;
    pool[header->right].left = header->left;
    // traitement des noeuds
    for (Node* iter = &pool[header->down]; iter != header; iter = &pool[iter->down])
    {
        for (Node* iter2 = &pool[iter->right]; iter2 != iter; iter2 = &pool[iter2->right])
        {
            pool[iter2->up].down = iter2->down;
            pool[iter2->down].up = iter2->up;
            pool[iter2->data.head].data.size--;
        }
    }
}

void uncover (Node* header)
{
    // traitement des noeuds
    for (Node* iter = &pool[header->up]; iter != header; iter = &pool[iter->up])
    {
        for (Node* iter2 = &pool[iter->left]; iter2 != iter; iter2 = &pool[iter2->left])
        {
            pool[iter2->up].down = iter2 - root_;
            pool[iter2->down].up = iter2 - root_;
            pool[iter2->data.head].data.size++;
        }
    }
    // restaure le header
    pool[header->left].right = header - root_;
    pool[header->right].left = header - root_;
}

bool search (Node* root)
{
    if (root->right == 0)
        return true;

    // recherche la colonne avec le moins de noeuds
    Node* header = &pool[root->right];
    for (Node* iter = header; iter != root; iter = &pool[iter->right])
    {
        //hack: si une colonne est vide, aucune solution n'est possible
        if (iter->data.size == 0)
        {
            return false;
        }
        if (iter->data.size < header->data.size)  // first comparison is useless
        {
            header = iter;
        }
    }

    bool ret = false;

    // procedure
    cover(header);
    for (Node* iter = &pool[header->down]; iter != header; iter = &pool[iter->down])
    {
        for (Node* iter2 = &pool[iter->right]; iter2 != iter; iter2 = &pool[iter2->right])
            cover(&pool[iter2->data.head]);

        if (search(root))
        {
            ret = true;
            // Hack: the node relative address gives the answer
			uint16_t x = (iter - nodes_) / 4;
			uint16_t i = x / (N_2*N_2);
			uint16_t j = (x % (N_2*N_2)) / N_2;
			uint16_t val = (x % N_2) + base;
			solution[i][j] = val;
        }

        for (Node* iter2 = &pool[iter->left]; iter2 != iter; iter2 = &pool[iter2->left])
            uncover(&pool[iter2->data.head]);

        if (ret)
            break;
    }
    uncover(header);

    return ret;
}

void affichage (char g[N_2][N_2+1], FILE *stream)
{
    for (int i=0; i<N_2; i++)
    {
        fputs(g[i], stream);
        fputc('\n', stream);
    }
}

void add_row (unsigned l, unsigned c, char val)
{
    unsigned pos[4];
    unsigned k = val-base;
    // calcule les positions pour les contraintes
    pos[0] = (l*N_2)+c;
    pos[1] = (l*N_2)+k;
    pos[2] = (c*N_2)+k;
    pos[3] = ((N*(l/N)+c/N)*N_2)+k;
    // ajoute les contraintes au dancing links
    Node* last = NULL;
    for (unsigned i=0; i < 4; i++)
    {
        Node* nd = &nodes_[(l*N_2*N_2+c*N_2+k)*4+i];
        InitNode(&headers_[i*N_2*N_2+pos[i]], last, nd);
        last = nd;
    }
}

Node* init(char g[N_2][N_2+1]) {
    // cree la racine
    Node* root = root_;
    InitRoot(root);

    // cree les headers
    unsigned i;
    for (i=1; i <= 4*N_2*N_2; ++i)
    {
        Node * header = &pool[i];
        header->left = i - 1;
        header->up = header->down = i;
        // initialise nbElements
        header->data.size = 0;
        pool[i-1].right = i;
    }
    pool[i].right = 0;  // root
    root->left = i;

    for (unsigned l=0; l < N_2; l++)
    {
        for (unsigned c=0; c < N_2; c++)
        {
            const char v = g[l][c];
            if (v != vide)
                add_row(l, c, v);
            else for (char val=base; val < base+N_2; val++)
                add_row(l, c, val);
        }
    }

    return root;
}

int main (void)
{
    char grille[N_2][N_2+1];

    for (unsigned l=0; l < N_2; l++)
    {
        char line[N_2 + 1];
        scanf("%[^\n]", line);
        fgetc(stdin);
        strncpy(grille[l], line, N_2 + 1 );
        //grille[l][N_2] = '\0';
    }

    //affichage(grille, stderr);

    Node *root = init(grille);
    bool ok = search(root);

    affichage(solution, stdout);

    return 0;
}
