#-*- coding:utf-8 -*-

import func

def main():

    args = func.get_args()

    if hasattr(args, 'file'):
        print(args.file)

    func.write_file((func.chop_categoly(func.get_file(args.file))))

# main関数呼び出し
if __name__ == "__main__":
    main()