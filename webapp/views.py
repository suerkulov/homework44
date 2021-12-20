from django.shortcuts import render
# from Exceptions import ValueError
# Create your views here.

list_cows = []
list_bulls = []




def check_view(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    if request.method == 'POST':

        secret_nums = [5, 1, 2, 9]
        bulls = 0
        cows = 0
        nums = request.POST.get('input_nums')
        nums = nums.split(" ")
        words = ""
        context = {'words': ''}
        try:
            for i in nums:
                i = int(i)
                if 9 < i < 0:
                    words = "number must be less than 9 and larger than 0"
            a = set(nums)
            if len(a) < 4:
                words = "number must not be equal"
            elif len(a) > 4:
                words = "count of numbers must be 4"
            elif nums == secret_nums:
                words = "You got it right!"

            else:
                for i in range(len(secret_nums)):
                    if secret_nums[i] == int(nums[i]):
                        bulls += 1
                    elif int(nums[i]) in secret_nums:
                        cows += 1
            list_cows.append(cows)
            list_bulls.append(bulls)
            list_rounds.append(round)
            words = f"You got {bulls} bulls, {cows} cows"

        except ValueError:
            words = 'Вводите числа'

        context['words'] = words
        return render(request, 'index.html', context)


def game_history(request):
    count_bulls = list_bulls[0]
    if count_bulls is None:
        count_bulls = 0
    count_cows = list_cows[0]
    if count_cows is None:
        count_cows = 0
    context = {
        'count_bulls': count_bulls,
        'count_cows': count_cows
    }
    return render(request, 'history.html', context)

