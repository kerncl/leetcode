#Question: Easy
'''
Given an array A of strings made only from lowercase letters, return a list of all characters that show up in all strings within the list (including duplicates).  For example, if a character occurs 3 times in all strings but not 4 times, you need to include that character three times in the final answer.
You may return the answer in any order.
'''
from typing import List


class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        for _, word in enumerate(A):
            if not _:
                common = word
            else:
                common = set(common).intersection(word)
        final_common = list(common)
        for char in common:
            is_append = True
            if A[0].count(char) > 1:
                temp_char = [A[0].count(char)]
                for index in range(1,len(A)):
                    temp_char.append(A[index].count(char))
                    if 1 in temp_char:
                        is_append = False
                        break
                if is_append:
                    if 2 not in temp_char:
                        temp_char.sort()
                        temp_list = [char]*(temp_char[0]-1)
                        final_common.extend(temp_list)
                    else:
                        final_common.append(char)
        return final_common


A = ["dbcdjbedfchcbhbecbadeaefefhcaagfghjaidaadeaabaaegj","hfacgbgcieccadeejddegjffejdjegejbaddaiabdhahbjaiba","igfaddihhceieadjgjhefaibcfcichcdecjcihfhcgfjeihidf","jaehjjibbhfdcjjdhecicefjjjdabibahgdaeibfefbbffhjja","degddigjijggagjgaaeeegfiahhcghbefcbdabeehbihjdeabi","bjdfedddebaifgadhgdhfjjdafajhiabbjjiidhcdaagajiafh","ihfjgjjcfeebebjgihdejjdheaeeddiajffjjdbfcfdaabgcei","jdbhhhigagieacgdabbchegdaefgeebaccdeajiifgfecbdgig","djhghabfejhcgbdejfcafjbagecbdggehaaddicgejhdgdahaf","hbaaccbffecibeiabdfeggbahbiehjiejifjjjbbbiiejcejdf","fadeddbhjehehhjiiehigjdaaiaaebjdaicbefacedfcgbegge","djhidhibeghjfbdgabgeejgedifdageichiijachhjfeihfieb","jdiagceichahjbjadhagegbbedhijhgefhfcbhdeefeahghfde","chhbbaeaeacaccbjiegfadfhabbchjggidahbgdhcadafjfifa","cdiabdbeaeefjiaadigdgiihajgcbghcfdhicjjfeiciaidjfh","gfehabegchgidgjbhdighfjbeajhdfaebificjaeahiajjgeab","agafjbjjhadjaichgfihehdhfaiiaffbijeahegjgfcidhhbed","gchagffchcjjadhbhhjfiiagejchbgjabadjcbdigdfdfabgee","ciacjdahajifafhbfbdaddbgbddedhjbbbdbbbfhcidfcbiijg","dbjjbajjgehcbgfaibjjcbigaijdjaagbfbfcjebahjchdfacg","bgfifecddgcfefijhccjiaiedhaeahihehiaedjfebejceibid","hiiigbiddhhejdebjcgjgdfiaijieibbaiibecbjigadejaibj","hafbbjafdjahdhdfiafedjjdgjghcfffcjedgjeffbeahfgbcf","bfcjigdiadjhfjjbghcdhchgaiefdijgcbbcjfaehccgddigah","aehfeiccfieaihijcgfahceadeiffefiegciageeaieghadgda","eafcdbagdafjdbicbabhihfhiefdiehhiiijigfhajfcbgajff","ecgdieegbfcijifhgicihhfhgbebgbjiiegbbfhijbcbecgigd","idhjgaccgaaieidbeidbcadhidhdddgjceccjgehjcidebeidi","bchhdjiiacccidhhcbchehcaddeccfecbcedidhhbjcigddhfg","ieddgabeciffjfchdggifjcebadchbdcdgiagefhecifgifdcj","bedcfhjehehdhafeadbdffbadjhgefjdchjghjedhgadihaedc","cfhcigdaaaddfjifaadejdgdfdfdhfebicfedcefbcgbbdbibh","jbddeaghjegebciaihfjffceiaehgaeecijefafficbajehgej","dbejheeaeadbaifegcjjhahggdbgjbeieghbeijjedjdbfiecc","dgdbefabibgeehgbdjggidagdfhjdgahbjidgejjfgcafcjddf","hcbaggjggcbcgjbceihbghdhbediacdfgfheghddecedddjggf","cdhhaaieachbfgcigidjfjcihecdegifedhadgacieciihafhf","hhicegfcdihbddjaibadeacbjdjjhjdeegjjaedgjegbbbbifg","bjcggafgaajegfcihfaicfhcdfdhgfegjfcbadighbciadhcfd","cabdajhgciaihgdccghbjcbgfighjideehbejjhhihgdjebgje","caaafahejcbedgibhadcfddaejhhaaicejefeghjhijcbfaegd","fggbheafgcbgdcfibiajdachcifhcfdfebbfcjfgefebebbdcc","gdiabbdaicaijehcjhhibbeeidjdjicdbddiaacciehehdbhch","ddbahiacdhccafecfhihfhdeicghdjbfbdehcjdhjhjehdfjhc","hadjggchcjdfaaicggigjgjaeegjfccccejeghbfcgajeccfee","ghcafaieijddfiebcibdccjijafiieeidjdiadbcjhbdjaeiec","gdfjagafhcaihhejfjcjecccfbcidhcidffebcigjdbafjgieh","ifafgibebjghgiaachefhggeibejfdhfaiciighejbiahiihii","caecdaaihahejaidgcecejgcdfhhdeghjacgeaefhjbijbbhgh","hhfdeajjijgeechaieehfcfjaaaadjbejibjfajijcfhicbjhb"]
result = Solution()
print(f'Common Char: {result.commonChars(A)}')
