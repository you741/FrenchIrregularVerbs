#This is an irregular verb present conjugation test program
#NOTE: For essayer, there are technically 2 correct answers for je, tu,
#il, elle, ils, elles but I only used one.
def ask(num):
    global bank
    straight = False
    if len(bank) > 0:
        straight = True
    done = []
    total = 0
    for i in range(num):
        verb,subject = "",""
        if not straight:
            while True:
                rv = randint(0,len(verbs)-1)
                rs = randint(0,5)
                if (rv,rs) not in done:
                    done.append((rv,rs))
                    verb = verbs[rv]
                    subject = subj[rs]
                    break
        else:
            rv,rs = bank[len(bank)-i-1]
            del bank[len(bank)-i-1]
            verb,subject = verbs[rv],subj[rs]
        ans = conju[verb][rs]
        u_ans = input("Conjugate "+verb+" ("+subject+"): ").lower()
        if (ans == u_ans) or (ans == "essaie" and u_ans == "essaye") or (ans == "essaies" and u_ans == "essayes"):
            total += 1
            print("Correct!")
        else:
            bank.append((rv,rs))
            print("Wrong! The correct answer was",ans)
    print(total/num*100,"% right")
    if len(bank)>0:
        cont = input("Redo wrong words? [Y/N]").lower()
        if cont == "y":
            return True
    return False
from random import *
conju = {"avoir":["ai","as","a","avons","avez","ont"],
         "être":["suis","es","est","sommes","êtes","sont"],
         "aller":["vais","vas","va","allons","allez","vont"],
         "faire":["fais","fais","fait","faisons","faites","font"],
         "prendre":["prends","prends","prend","prenons","prenez","prennent"],
         "venir":["viens","viens","vient","venons","venez","vont"],
         "mourrir":["meurs","meurs","meurt","mourons","mourez","meurent"],
         "commencer":["commence","commences","commence","commençons","commencez","commencent"],
         "préférer":["préfère","préfères","préfère","préférons","préférez","préfèrent"],
         "devoir":["dois","dois","doit","devons","devez","doivent"],
         "pouvoir":["peux","peux","peut","pouvons","pouvez","peuvent"],
         "vouloir":["veux","veux","veut","voulons","voulez","veulent"],
         "ouvrir":["ouvre","ouvres","ouvre","ouvrons","ouvrez","ouvrent"],
         "partir":["pars","pars","part","partons","partez","partent"],
         "dormir":["dors","dors","dort","dormons","dormez","dorment"],
         "voir":["vois","vois","voit","voyons","voyez","voient"],
         "essayer":["essaie","essaies","essaie","essayons","essayez","essaient"],
         "s'asseoir":["m'assieds","t'assieds","se assied","nous asseyons","vous asseyez","se asseyent"],
         "mentir":["mens","mens","ment","mentons","mentez","mentent"],
         "sentir":["sens","sens","sent","sentons","sentez","sentent"],
         "mettre":["mets","mets","met","mettons","mettez","mettent"],
         "battre":["bats","bats","bat","battons","battez","battent"],
         "convaincre":["convaincs","convaincs","convainc","convainquons","convainquez","convainquent"],
         "craindre":["crains","crains","craint","craignons","craignez","craignent"],
         "croire":["crois","crois","croit","croyons","croyez","croient"],
         "lever":["lève","lèves","lève","levons","levez","lèvent"],
         "mener":["mène","mènes","mène","menons","menez","mènent"],
         "prendre":["prends","prends","prend","prenons","prenez","prennent"],
         "connaître":["connais","connais","connaît","connaissons","connaissez","connaissent"],
         "conduire":["conduis","conduis","conduit","conduisons","conduisez","conduisent"],
         "recevoir":["reçois","reçois","reçoit","recevons","recevez","reçoivent"],
         "écrire":["écris","écris","écrit","écrivons","écrivez","écrivent"],
         "savoir":["sais","sais","sait","savons","savez","savent"],
         "acheter":["achète","achètes","achète","achetons","achetez","achètent"],
         "jeter":["jette","jettes","jette","jetons","jetez","jettent"],
         "espérer":["espère","espères","espère","espérons","espérez","espèrent"],
         "vivre":["vis","vis","vit","vivons","vivez","vivent"],
         "boire":["bois","bois","boit","buvons","buvez","boivent"],
         "suivre":["suis","suis","suit","suivons","suivez","suivent"],
         "dire":["dis","dis","dit","disons","dites","disent"],
         "lire":["lis","lis","lit","lisons","lisez","lisent"],
         "courir":["cours","cours","court","courons","courez","courent"],
         "appeler":["appelle","appelles","appelle","appelons","appelez","appellent"],
         "manger":["mange","manges","mange","mangeons","mangez","mangent"]}
verbs = list(conju.keys())
subj = ["je","tu","il/elle/on","nous","vous","ils/elles"]
num = max(min(int(input("Enter # questions: ")),6*len(verbs)-1),0)
bank = []
while True:
    if not ask(num):
        break
    else:
        num = len(bank)

         
