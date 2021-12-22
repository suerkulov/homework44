from django.shortcuts import render
# from Exceptions import ValueError
# Create your views here.


secret_nums = [5, 1, 2, 9]
main_list = []


def first_check_view(nums):
    for i in nums:
        if 9 < i < 0:
            return "number must be less than 9 and larger than 0"
    a = set(nums)
    if len(a) > 4:
        return "count of numbers must be less than 4"
    if len(a) < 4:
        return "count of numbers must be more than 4"
    bulls = 0
    cows = 0
    for i in range(len(nums)):
        if nums[i] == secret_nums[i]:
            bulls += 1
        elif nums[i] in secret_nums:
            cows += 1
    if bulls == len(secret_nums):
        return "You won!"
    return f"You got {bulls} bulls and {cows} cows"


def index_view(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    elif request.method == "POST":
        try:
            numbers = list(map(int, request.POST.get('input_nums').split(' ')))
            words = first_check_view(numbers)
            print(words)
        except ValueError:
            words = "enter numbers int"
            print(words)
        context = {
            'words': words
        }
        main_list.append(words)
        return render(request, 'index.html', context)


def history_view(request):
    llist = []
    for i in enumerate(main_list, start=1):
        llist.append(i)
    context = {
        'llist': llist
    }
    return render(request, 'history.html', context)