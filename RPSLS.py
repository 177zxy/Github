#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ�������
���ڣ�2021.11.27
"""
import random
def name_to_number(name):
    """
    ����Ϸ�����Ӧ����ͬ������
    """
    if name=="ʯͷ":
        play_number=0
    elif name=="ʷ����":
        play_number=1
    elif name=="ֽ":
        play_number=2
    elif name=="����":
        play_number=3
    elif name=="����":
        play_number=4
    else :
        print("Error: No Correct Name")
    return play_number




    # ʹ��if/elif/else��佫����Ϸ�����Ӧ����ͬ������
    # ��Ҫ���Ƿ��ؽ��




def number_to_name(number):
    """
    ������ (0, 1, 2, 3, or 4)��Ӧ����Ϸ�Ĳ�ͬ����
    """
    if number==0:
        comp_name="ʯͷ"
    elif number==1:
        comp_name="ʷ����"
    elif number==2:
        comp_name="ֽ"
    elif number==3:
        comp_name="����"
    elif number==4:
        comp_name="����"
    else :
        print("Error: No Correct Name")
    return comp_name
    # ʹ��if/elif/else��佫��ͬ��������Ӧ����Ϸ�Ĳ�ͬ����
    # ��Ҫ���Ƿ��ؽ��




def rpsls(player_choice):
    """
    �û�����������һ��ѡ�񣬸���RPSLS��Ϸ��������Ļ�������Ӧ�Ľ��

    """
    play_number=name_to_number(player_choice)
    print("--------")
    print("���������ѡ��",player_choice)
    comp_number=random.randrange(5)
    comp_choice=number_to_name(comp_number)
    print("�������ѡ��",comp_choice)
    if play_number==comp_number:
        print("���ͼ��������һ����")
    elif (play_number==0 and comp_number>=3) or (play_number==1 and comp_number==0) or(play_number==1 and comp_number== 4) or (play_number==2 and comp_number==0) or(play_number==2 and comp_number== 1) or (play_number==3 and comp_number==1) or(play_number==3 and comp_number== 2) or (play_number==4 and comp_number==2) or( play_number==4 and comp_number==3) :
        print("��Ӯ��")
    else:
        print("�����Ӯ��")

    # ���"-------- "���зָ�

    # ��ʾ�û�������ʾ���û�ͨ�����̽��Լ�����Ϸѡ��������룬�������player_choice

    # ����name_to_number()�������û�����Ϸѡ�����ת��Ϊ��Ӧ���������������player_choice_number

    # ����random.randrange()�Զ�����0-4֮��������������Ϊ��������ѡ�����Ϸ���󣬴������comp_number

    # ����number_to_name()����������������������ת��Ϊ��Ӧ����Ϸ����

    # ����Ļ����ʾ�����ѡ����������

    # ����if/elif/else ��䣬����RPSLS������û�ѡ��ͼ����ѡ������жϣ�������Ļ����ʾ�жϽ��

    # ����û��ͼ����ѡ��һ��������ʾ�����ͼ��������һ���ء�������û���ʤ������ʾ����Ӯ�ˡ�����֮����ʾ�������Ӯ�ˡ�




# �Գ�����в���
print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
print("����������ѡ��:")
choice_name=input()
rpsls(choice_name)
