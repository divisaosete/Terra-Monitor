import{readFile,writeFile}from'node:fs/promises';
let text=await readFile('assets/app.js','utf8');
text=text.replace("q?format(q.rows.length):'—'","q?.time?format(q.rows.length):'—'").replace("state.data.alerts?format(state.data.alerts.rows.length):'—'","state.data.alerts&&(state.data.alerts.rows.length||!state.data.alerts.failed)?format(state.data.alerts.rows.length):'—'").replace("state.data.alerts?format(rows.length):'—'","state.data.alerts&&(rows.length||!state.data.alerts.failed)?format(rows.length):'—'").replace("${state.data.alerts?'Os comunicados","${state.data.alerts?.rows.length?'Os comunicados");
text=text.replace("key==='alerts'?'Último comunicado emitido':'Observação de referência'","key==='alerts'?'Último comunicado emitido':key==='weather'?'Condição estimada para':'Observação de referência'");
await writeFile('assets/app.js',text);
