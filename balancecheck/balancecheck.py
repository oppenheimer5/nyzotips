from requests import get
try:
    my_nodes, total, cnt = [line.rstrip('\n') for line in open('public.txt')], 0, 0
except FileNotFoundError as e:
    print(str(e) + ' - you need a file in this directory called public.txt')
    exit(1)
for line in get('http://nyzo.co/block/last').text.splitlines():
    if line.find('var initialBlockHeight') > 0:
        current_block = int(line.split('initialBlockHeight = ')[1].split(';')[0])
print('Nyzo is currently at block %i' % current_block)
for line in get('https://nyzo.co/balanceListPlain/' + str(current_block)).text.split('<p>'):
    if line.split("     ")[0] in my_nodes:
        try:
            print("Wallet %i: " % cnt + line.split("     ")[0][:4] + '...' + line.split("     ")[0][-5:] + ' - '+ line.split("     ")[1].strip(u"\u2229") + ' nyzo')
            total += float(line.split("     ")[1].strip(u"\u2229"))
            cnt += 1
        except:
            pass
print("Total: {0:.2f} nyzo".format(total))
