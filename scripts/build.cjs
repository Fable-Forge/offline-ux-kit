const fs=require('node:fs'),path=require('node:path');
const root=path.resolve(__dirname,'..'),kit=require('../assets/offline-ux.js');
const runtime=fs.readFileSync(path.join(root,'assets/offline-ux.js'),'utf8').replace(/<\/script/gi,'<\\/script');
const template=fs.readFileSync(path.join(root,'examples/demo.html'),'utf8');
fs.mkdirSync(path.join(root,'dist'),{recursive:true});
for(const mode of ['form','dialogue']) fs.writeFileSync(path.join(root,'dist',mode+'.html'),template.replace('/*__RUNTIME__*/',()=>runtime).replaceAll('__MODE__',mode));
fs.writeFileSync(path.join(root,'dist/review.html'),kit.reviewer());
const events=[];
function add(name,stepId,data={}){events.push({eventId:'sample-'+events.length,seq:events.length+1,timestamp:'2026-09-10T00:00:00Z',elapsedMs:events.length*2000,sincePreviousMs:2000,name,stepId,taskId:'sample-form',taskRunId:'task-1',data});}
add('run_start','');add('task_start','');add('step_enter','preferences');add('choice','preferences',{optionId:'a',changed:false});add('time_slice','preferences',{activeMs:8000,visibleMs:8000,hiddenMs:0});add('back','preferences');add('choice','preferences',{optionId:'b',previousOptionId:'a',changed:true});add('feedback','preferences',{category:'unclear'});add('step_enter','review');add('time_slice','review',{activeMs:8000,visibleMs:8000,hiddenMs:0});add('task_end','review',{status:'completed'});add('run_end','');
const sample={meta:{schemaVersion:1,kitVersion:kit.VERSION,appId:'sample',participantId:'synthetic-example',sessionId:'sample-1',buildId:'demo',batchId:'synthetic',variant:'offline-scripted',startedAt:'2026-09-10T00:00:00Z',endedAt:'2026-09-10T00:01:00Z',storageMode:'memory'},events};
fs.writeFileSync(path.join(root,'dist/sample.json'),JSON.stringify(sample,null,2));
fs.writeFileSync(path.join(root,'dist/sample-report.html'),kit.report(sample));
console.log('Built form, dialogue, reviewer, synthetic JSON and report.');
