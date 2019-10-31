#!/usr/bin/env python
import argparse

class Lineup:
    def __init__(self, qb, dst, k, rb, wr, te):
        self.qb = qb
        self.dst = dst
        self.k = k
        self.rb = rb
        self.wr = wr
        self.te = te


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate Fantasy Ticket Lineups')
    parser.add_argument('--qb', type=str, action='append')
    parser.add_argument('--dst', type=str, action='append')
    parser.add_argument('--k', type=str, action='append')
    parser.add_argument('--rb', type=str, action='append')
    parser.add_argument('--wr', type=str, action='append')
    parser.add_argument('--te', type=str, action='append')

    args = parser.parse_args()
    qb = args.qb
    dst = args.dst
    k = args.k
    rb = args.rb
    wr = args.wr
    te = args.te

    lineups = [Lineup('QB', 'DST', 'K', 'RB', 'WR', 'TE'), Lineup('--','---','-','--','--','--')]

    for a in qb:
        for b in dst:
            for c in k:
                for d in rb:
                    for e in wr:
                        for f in te:
                            lineups.append(Lineup(a,b,c,d,e,f))

    lineups.append(Lineup('--','--','--','--','--','--'))

    qbl = '{{:^{}}}'.format(len(max(qb, key=len)))
    dstl = '{{:^{}}}'.format(len(max(dst, key=len)))
    kl = '{{:^{}}}'.format(len(max(k, key=len)))
    rbl = '{{:^{}}}'.format(len(max(rb, key=len)))
    wrl = '{{:^{}}}'.format(len(max(wr, key=len)))
    tel = '{{:^{}}}'.format(len(max(te, key=len)))

    fmt = '| {} | {} | {} | {} | {} | {} |'.format(qbl,dstl,kl,rbl,wrl,tel)

    for l in lineups:
        print(fmt.format(l.qb,l.dst,l.k,l.rb,l.wr,l.te))

    cost = (len(lineups) - 3) * 5

    print('| total cost: ${}'.format(cost))
