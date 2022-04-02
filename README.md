# pdf-to-anki-occlusion-notes
this project uses razer macros and python to send selected text to anki in the form of closed deletion notes, with support for multiple closed deletions on the same note
## Installation 
Clone the repository
Import provided razer macros and assing them to three mouse keys
![Screenshot 2022-04-01 213655](https://user-images.githubusercontent.com/87684029/161363517-b8382569-11cc-41fa-ad2a-34a24a775a0e.jpg)

## Set-up
Macros assume the following positioning of applications in your taskbar: Chrome as the first application, anki as the second and the to_be_processed.txt file open as the third item
![image](https://user-images.githubusercontent.com/87684029/161363436-30edde1f-913e-4b84-962a-756fb14e2f34.png)

## Using the software
to set the text of an anki note trigger the razer macro titled "text of note"
to create a new closed deletion trigger the razer macro titled "new close deletion"
to add a second part to an existing closed deletion trigger the razer macro titled "continue close deletion"*

* and example of continueing a closed deletion would be the following note: "A {{c2::pointer}} is usually drawn as a {{c1::box}}, and the {{c2::reference}} it stores is drawn as an {{c1::arrow}} starting in the box and leading to its {{c2::pointee}}." 
Here the text "A pointer is usually drawn as a box, and the reference it stores is drawn as an arrow starting in the box and leading to its pointee." would be selected as the "text of note" macro is triggered
then the text "box" and "arrow" would be selected in turn while triggering the "continue close deletion" macro
then the text "pointer" would be selected as the "new close deletion" macro is triggered
and finally the text "pointee" would be selected while triggering the "continue close deletion" macro
## Importing software generated notes to anki
after the to_be_processed.txt file is fully populated with the desiered notes
1. save the document
2. run "strings_to_anki_notes.py"
3. go to anki and follow the prompts to import a file
4. select "to_be_imported.txt"
5. set type to Cloze
6. select location to be imported to
7. change the "Feild seperated by" option to "\t"
8. click import
9. clear the to_be_processed file for next use
