import{readFile,writeFile}from'node:fs/promises';
const html=await readFile('index.html','utf8');
await writeFile('tests/offline.html',html.replaceAll('href="./','href="../').replaceAll('src="./','src="../').replace('<head>','<head><script>Object.defineProperty(window,"localStorage",{value:{getItem:()=>null,setItem:()=>{},removeItem:()=>{}}});window.fetch=async()=>{throw Error("Falha de rede simulada em teste isolado")};</script>'));
console.log('Teste isolado criado em tests/offline.html; não contém dados simulados.');
