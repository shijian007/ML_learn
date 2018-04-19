# -*- coding: cp936 -*-

import os, codecs, random
from math import sqrt

#���õ��Ľ�������ֵ���
rows_norms = {}
def readfile(dirname):
    rows = {}
    for f in os.listdir(dirname):
        fr = codecs.open(dirname + f,'r',encoding = 'utf-8')
        tw_dict = {}
        norm = 0
        for line in fr:
            items = line.split('\t')
            token = items[0].strip()
            if len(token)<2:
                continue
            w = float(items[1].strip())
            norm = w**2
            tw_dict[token] = w
        rows[str(f[:-4])] = tw_dict
        rows_norms[str(f[:-4])] = sqrt(float(norm))
    #print len(rows)
    return rows

#�õ����Ҿ��룬����v1����row,v2�Ǿ������ĵ�
def cosine(v1,norm_v1,v2,norm_v2):
    if norm_v1 == 0 or norm_v2 == 0:
        return 1.0
    dividend = 0
    for k,v in v1.items():
        for k in v2:
            dividend += v*v2[k]
    return 1.0-dividend/(norm_v1*norm_v2)

#�㷨��ʵ��
def kcluster(rows,distance=cosine,k=3):
    ranges = rows_range(rows)
    #��ʼ����������
    clusters=[]
    for i in range(k):
        clusters.append(random_vec(ranges))

    clusteres_norm=[]
    for i in range(k):
        clusteres_norm.append(norm(clusters[i]))
    lastmatches=None
    #��ʼ����
    for t in range(300):
        print '��%d�ε���' % t
        bestmatches=[[] for i in range(k)]
        for j in rows.keys():
            row=rows[j]
            row_norm=rows_norms[j]
            bestmatch=0
            min_dis=10000000
            for i in range(k):
                d=distance(row, row_norm, clusters[i],clusteres_norm[i])
                if d<min_dis:
                    bestmatch=i
                    min_dis=d
            bestmatches[bestmatch].append(j)
        if bestmatches==lastmatches:
            break
        lastmatches=bestmatches
        for i in range(k):
            clusters[i] = center(bestmatches[i], rows)
    print bestmatches
    return bestmatches

#test
if __name__ == '__main__':
    corpus_dir='E:/study/Recommendation-System/algorithm/keyword'
    rows=readfile(corpus_dir)
    print 'create vectorspace'
    n=3
    clust=kcluster(rows,k=n)