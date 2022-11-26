// KEY
// t --> note text --> ת
// n --> new close deletion --> נ
// c --> continue close deletion --> כ
const CARD_SEPERATOR = '\n'	

// Stores and content of text as a cookie every 10 seconds when the user has more than 21 words or when triggered manually. 
const saveToCookies = (draft_text: string) => document.cookie = 'draft_text='+draft_text+`;max-age=${60 * 60 * 24 * 14};`;
const getFromCookies = () => document.cookie.split("=")[1] // Because only one cookie is ever stored it is very simple to acsess
setInterval(() => {
	const text= document.getElementById("text-val") as HTMLTextAreaElement | null; // Content of text area user pastes unconverted anki notes into
	if (text.value.split(" ").length > 20) saveToCookies(text.value)
}, 10000); // Auto save


// Triggered by user, dowloads a text file with incerted close deletions ({{c1::_________}})
function saveTextFile(): void {
	const text= document.getElementById("text-val") as HTMLTextAreaElement | null;
	const filename = document.getElementById("file-name") as HTMLInputElement | null;
	download(filename.value, convert_to_anki(text.value));
}

// TODO rewrite in my own words
function download(filename:string, text:string): void {
	var element = document.createElement('a');
	element.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(text));
	element.setAttribute('download', filename);

	element.style.display = 'none';
	document.body.appendChild(element);

	element.click();
	document.body.removeChild(element);
	}


// Given a string containing the following flag characters return a string containing close deletions
// 	--- KEY ---
// 	t --> note text --> ת
//	n --> new close deletion --> נ
//	c --> continue close deletion --> כ
const convert_to_anki = (original_text:String) =>
	note_with_flag_characters_to_list_tree(original_text).map(function(val){
		let anki_note = val.shift().shift()
		const cards:Array<Array<String>> = val.slice(1)
		cards.forEach(function callback(value, index) {
			const card = {"index": index + 1, "value": value}
			card["value"].forEach(close_deletion => {
				anki_note = anki_note.replaceAll(close_deletion.slice(0,-1), "{{"+card["index"]+"::" +close_deletion.slice(0,-1)+"}}")
			})
		});
		return anki_note
	      }).join(CARD_SEPERATOR)+CARD_SEPERATOR;


// top level is the note (all text in note 1)
// 	second level is each close deletion number (all the close deletions in card 1)
// 		third level is each close deletion (close deletion #1 that makes up part of card 1)
const note_with_flag_characters_to_list_tree = (original_text) => 
	original_text.replace(/\t|\n/gi, "") // remove tabs and new lines
		.split(/ת/gi).slice(1).map(x => x
			.split(/נ/gi)?.map(x => x
				.split(/כ/gi)))