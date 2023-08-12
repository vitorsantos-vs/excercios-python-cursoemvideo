num_pt = ("zero","um","dois","três","quatro","cinco","seis","sete","oito","nove","dez","onze","doze","treze","quatorze","quinze","dezesseis","dezessete","dezoito","dezenove","vinte","vinte e um","vinte e dois","vinte e três","vinte e quatro","vinte e cinco","vinte e seis","vinte e sete","vinte e oito","vinte e nove","trinta","trinta e um","trinta e dois",
"trinta e três","trinta e quatro","trinta e cinco","trinta e seis","trinta e sete","trinta e oito","trinta e nove","quarenta","quarenta e um","quarenta e dois","quarenta e três","quarenta e quatro","quarenta e cinco","quarenta e seis","quarenta e sete","quarenta e oito","quarenta e nove","cinquenta","cinquenta e um","cinquenta e dois","cinquenta e três","cinquenta e quatro","cinquenta e cinco","cinquenta e seis","cinquenta e sete","cinquenta e oito","cinquenta e nove","sessenta","sessenta e um","sessenta e dois","sessenta e três","sessenta e quatro","sessenta e cinco","sessenta e seis","sessenta e sete","sessenta e oito","sessenta e nove","setenta","setenta e um","setenta e dois","setenta e três","setenta e quatro","setenta e cinco","setenta e seis","setenta e sete","setenta e oito","setenta e nove","oitenta","oitenta e um","oitenta e dois","oitenta e três","oitenta e quatro",
"oitenta e cinco","oitenta e seis","oitenta e sete","oitenta e oito","oitenta e nove","noventa","noventa e um","noventa e dois","noventa e três","noventa e quatro","noventa e cinco","noventa e seis","noventa e sete","noventa e oito","noventa e nove","cem")

num_en = ("zero","one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen","twenty","twenty-one","twenty-two","twenty-three","twenty-four","twenty-five","twenty-six","twenty-seven","twenty-eight","twenty-nine","thirty","thirty-one","thirty-two","thirty-three",
"thirty-four","thirty-five","thirty-six","thirty-seven","thirty-eight","thirty-nine","forty","forty-one","forty-two","forty-three","forty-four","forty-five","forty-six","forty-seven",
"forty-eight","forty-nine","fifty","fifty-one","fifty-two","fifty-three","fifty-four","fifty-five","fifty-six","fifty-seven","fifty-eight","fifty-nine","sixty","sixty-one","sixty-two","sixty-three","sixty-four","sixty-five","sixty-six","sixty-seven","sixty-eight","sixty-nine","seventy","seventy-one","seventy-two","seventy-three","seventy-four","seventy-five","seventy-six","seventy-seven","seventy-eight","seventy-nine","eighty","eighty-one","eighty-two","eighty-three","eighty-four","eighty-five","eighty-six","eighty-seven","eighty-eight","eighty-nine","ninety","ninety-one","ninety-two","ninety-three","ninety-four","ninety-five","ninety-six","ninety-seven","ninety-eight","ninety-nine","one hundred")


while True:
    num = int(input('Digite uma numero entre 0 e 100: '))
    if 0 <= num <= 100:   
        print(f'Voce digitou o numero {num_pt[num]} ({num}), em ingles é {num_en[num]}')      
        resp = ' '
        while resp not in 'SN':
            resp = input('Deseja continuar? [S/N] ').strip().upper()
        if resp == 'N':
            break
    else:    
        print('Tente novamente. ', end='')





