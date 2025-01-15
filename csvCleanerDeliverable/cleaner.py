import csv
import os
import pygame
import pygame.freetype
from pygame.locals import *
import sys

'''

#################### BEFORE YOU RUN THE PROGRAM ####################

Ensure that the undone file is titled "Contacts.csv" and saved as a
CSV file - also ensure that the headers are properly placed in the 
actual header area of the CSV file

####################################################################

'''

def cleanData(file):

    with open(file, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        with open('dataClean1.csv', 'w') as new_file:
        
            fieldnames = ['First Name', 'Last Name', 'Main Address', 'Email', 'Primary Phone', 'Zip Code', 'Secondary Phone']

            csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter=',')

            #Things taken out --> 'Client ID,Name,Main Address,Franchise,Phone,Job Title,Email,First Name,Last Name,Account,Phone 2,Primary Phone,Secondary Phone,Zip Code'

            csv_writer.writeheader()
        
            for line in csv_reader:
                if any(line):
                    del line['Client ID']
                    del line['Name']
                    del line['Phone']
                    del line['Phone 2']
                    del line['Franchise']
                    del line['Job Title']
                    del line['Account']
                    csv_writer.writerow(line)
    print('Data organization successful...')
    return 'dataClean1.csv'

#Everything bellow creates the new headers according to google's requirments'

with open('dataClean2.csv', 'w', newline='') as file:
    writer = csv.writer(file)

def convertFilesToGoogle(file):

    inputFileName = file
    outputFileName = 'dataClean2.csv'

    with open(inputFileName, 'r') as inFile, open(outputFileName, 'w') as outfile:
        r = csv.reader(inFile)
        w = csv.writer(outfile)

        next(r, None)

        w.writerow(['Given Name', 'Family Name' , 'Address 1 - Extended Address', 'E-mail 1 - Value', 'Phone 1 - Value', 'Address 1 - Postal Code', 'Phone 2 - Value'])

        for line in r:
                if any(line):
                    w.writerow(line)
        print('Final Clean Complete...')
        return 'dataClean2.csv'
    

convertFilesToGoogle(cleanData('Contacts.csv'))

pygame.init()

# Define window dimensions
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480

# Set up the display window
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Drag and Drop File")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Define text font
font = pygame.freetype.SysFont(None, 32)

def display_text(text):
    # Clear the window
    window.fill(WHITE)

    # Render the text
    text_render, text_rect = font.render(text, BLUE)
    text_render.blit_to(window, text_rect)
    text_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

    # Update the display
    pygame.display.update()

    # Return the text rect for collision detection
    return text_rect

# FILE CHUNKING PROCESS

chunk_size = 999

def write_chunk(part, lines):
    with open('dataFINAL'+ str(part) +'.csv', 'w') as f_out:
        f_out.write(header)
        f_out.writelines(lines)

with open('dataClean2.csv', "r") as f:
    count = 0
    header = f.readline()
    lines = []
    for line in f:
        count += 1
        lines.append(line)
        if count % chunk_size == 0:
            write_chunk(count // chunk_size, lines)
            lines = []
    # write remainder
    if len(lines) > 0:
        write_chunk((count // chunk_size) + 1, lines)
print('Final data chunking complete. ' + str(round(count/1000)) + ' files were created.')

write_chunk(0, convertFilesToGoogle(cleanData('Contacts.csv')))

'''
pygame.init()

fileFinal = 'lastFile.csv'

def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.DROPFILE:
                print('File received...')
                print(event.file)
                
                fileFinal = convertFilesToGoogle(cleanData(event.file))

                finalFunction()
                print('IT GOES HERE')
                pygame.quit()
                quit()


        # Update the display
        pygame.display.update()

main()
'''





'''

######### Benefits of the Program #########

    -Allows for quicker and better communication between mechanics/employees and customers
    -The customers get quicker more personlized responses
    -Each mechanic/employee saves about 15 minutes a day, and spared their annoyance at finding customers contacts
     and with 10 mechanics working each week - my program has saved the business and its employers

                    TIME SAVED CACLULATIONS

    -480 hours a week - worked by 10 employees and the 2 owners
    -15 mins * 12 employees * 7 days = 1260 minutes saved a week (21 hours a week)
    -Total percentage saved (21/480) = 4.375% SAVED EACH WEEK


'''
