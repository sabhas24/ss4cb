#include <stdio.h>
#include <stdlib.h>

void mg(int a[], int l, int m, int r)
{
    int ls = m - l + 1, rs = r - m;
    int lp, rp, mp;
    int *lt = (int *)malloc(ls * sizeof(int));
    int *rt = (int *)malloc(rs * sizeof(int));
    for (lp = 0; lp < ls; lp++)
        lt[lp] = a[l + lp];
    for (rp = 0; rp < rs; rp++)
        rt[rp] = a[m + 1 + rp];
    lp = 0;
    rp = 0;
    mp = l;
    while (lp < ls && rp < rs)
    {
        if (lt[lp] <= rt[rp])
            a[mp++] = lt[lp++];
        else
            a[mp++] = rt[rp++];
    }
    while (lp < ls)
        a[mp++] = lt[lp++];
    while (rp < rs)
        a[mp++] = rt[rp++];
    free(lt);
    free(rt);
}

void ms(int a[], int l, int r)
{
    if (l < r)
    {
        int m = l + (r - l) / 2;
        ms(a, l, m);
        ms(a, m + 1, r);
        mg(a, l, m, r);
    }
}
