from .base import Settings

def get_file_data(filename):
    datas =[]
    with open(filename) as file:
        data = file.read()
        datas.extend( data.split('\n') )

    return datas


def get_inputs():
    return get_file_data(Settings.get('base_path') + '/input.txt')

def get_outputs():
    return get_file_data(Settings.get('base_path') + '/output.txt')


def Submit(solve ):
    inputs = get_inputs()
    my_output = []
    for input in inputs:
        args = input.split(',')
        print(args)
        my_output.append( str(solve(*args)) )

    actual_output = get_outputs()

    wrong_count = 0
    for index in range(len(actual_output)):
        try:
            if actual_output[index] != my_output[index]:
                wrong_count += 1
                print("Expected %s, Yours %s" % ( actual_output[index], my_output[index] ) )
        except IndexError:
            print('Input / Output .txt wrong')


    total = len(actual_output)
    correct = total - wrong_count
    print('')
    print("Total %s, Correct %s, Wrong %s" % ( total, correct, wrong_count )  )
