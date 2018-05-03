import pygame
import math
import time

pygame.init()
#Set window size, caption
window = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Fractal Tree")
screen = pygame.display.get_surface()

#x1, y1是起点，angle是弯曲的角度，depth是重复的次数
def drawTree(x1, y1, angle, depth):
    #depth从9减到0，当0的时候if depth不成立，结束
    #递归要有终止条件，否则会栈溢出stackoverflow

    if depth:
        #算出下一个点的坐标
        x2 = x1 + int(math.cos(math.radians(angle)) * depth * 10.0)
        y2 = y1 + int(math.sin(math.radians(angle)) * depth * 10.0)
        #画出两个点之间的连线
        pygame.draw.line(screen, (255,255,255), (x1, y1), (x2, y2), 2)
        pygame.display.flip()
        #再次调用自己，算出接下来的点
        time.sleep(0.01)
        drawTree(x2, y2, angle - 20, depth - 1)
        drawTree(x2, y2, angle + 20, depth - 1)

def input(event):
    if event.type == pygame.QUIT:
        exit(0)

#调用函数，画出第一条线，然后自己循环
drawTree(300, 550, -90, 9)
#刷新页面

while True:
    input(pygame.event.wait())


'''
练习1，把树变胖/瘦；高/矮
练习2，让树左右弯曲
练习3，改变树的颜色
练习4，查找关于递归的知识，理解什么是递归
'''
