function out = model
%
% doisCilindros.m
%
% Model exported on May 4 2013, 14:16 by COMSOL 4.3.0.151.

import com.comsol.model.*
import com.comsol.model.util.*

model = ModelUtil.create('Model');

model.modelPath('D:\matematica\codigos_matlab\em');

model.modelNode.create('mod1');

model.geom.create('geom1', 2);

model.mesh.create('mesh1', 'geom1');

model.physics.create('es', 'Electrostatics', 'geom1');

model.study.create('std1');
model.study('std1').feature.create('stat', 'Stationary');
model.study('std1').feature('stat').activate('es', true);

model.geom('geom1').feature.create('c1', 'Circle');
model.geom('geom1').feature('c1').set('r', '0.001');
model.geom('geom1').run('c1');
model.geom('geom1').run('c1');
model.geom('geom1').feature.create('c2', 'Circle');
model.geom('geom1').feature('c2').set('r', '0.02');
model.geom('geom1').run('c2');
model.geom('geom1').feature('c2').set('type', 'curve');
model.geom('geom1').run('c2');
model.geom('geom1').run;

model.material.create('mat1');
model.material('mat1').propertyGroup('def').set('relpermittivity', {'1'});

model.physics('es').feature.create('gnd1', 'Ground', 1);

model.geom('geom1').feature('c1').set('createselection', 'on');
model.geom('geom1').feature('c2').set('createselection', 'on');

model.physics('es').feature.remove('gnd1');
model.physics('es').feature.create('gnd1', 'Ground', 1);
model.physics('es').feature('gnd1').selection.named('geom1_c1_bnd');
model.physics('es').feature.create('pot1', 'ElectricPotential', 1);
model.physics('es').feature('pot1').selection.named('geom1_c2_bnd');
model.physics('es').feature('pot1').set('V0', 1, '100');

model.mesh('mesh1').run;

model.sol.create('sol1');
model.sol('sol1').study('std1');
model.sol('sol1').feature.create('st1', 'StudyStep');
model.sol('sol1').feature('st1').set('study', 'std1');
model.sol('sol1').feature('st1').set('studystep', 'stat');
model.sol('sol1').feature.create('v1', 'Variables');
model.sol('sol1').feature('v1').set('control', 'stat');
model.sol('sol1').feature.create('s1', 'Stationary');
model.sol('sol1').feature('s1').feature.create('fc1', 'FullyCoupled');
model.sol('sol1').feature('s1').feature.remove('fcDef');
model.sol('sol1').attach('std1');

model.result.create('pg1', 'PlotGroup2D');
model.result('pg1').name('Electric potential');
model.result('pg1').set('data', 'dset1');
model.result('pg1').set('solrepresentation', 'solnum');
model.result('pg1').set('oldanalysistype', 'noneavailable');
model.result('pg1').set('data', 'dset1');
model.result('pg1').feature.create('surf1', 'Surface');
model.result('pg1').feature('surf1').name('Surface');
model.result('pg1').feature('surf1').set('data', 'parent');
model.result('pg1').feature('surf1').set('readytoplot', false);
model.result('pg1').feature('surf1').set('solrepresentation', 'solnum');
model.result('pg1').feature('surf1').set('expr', 'V');
model.result('pg1').feature('surf1').set('unit', '');
model.result('pg1').feature('surf1').set('descr', 'V');
model.result('pg1').feature('surf1').set('inheritplot', 'none');
model.result('pg1').feature('surf1').set('data', 'parent');
model.result('pg1').feature('surf1').set('expr', 'V');
model.result('pg1').feature('surf1').set('inheritplot', 'none');
model.result('pg1').feature('surf1').set('data', 'parent');
model.result('pg1').feature('surf1').set('expr', 'V');
model.result('pg1').feature('surf1').set('inheritplot', 'none');
model.result('pg1').feature('surf1').set('data', 'parent');
model.result('pg1').feature('surf1').set('expr', 'V');
model.result('pg1').feature('surf1').set('inheritplot', 'none');
model.result('pg1').feature('surf1').set('data', 'parent');
model.result('pg1').feature('surf1').set('expr', 'V');
model.result('pg1').feature('surf1').set('inheritplot', 'none');
model.result('pg1').feature('surf1').set('data', 'parent');

model.sol('sol1').runAll;

model.result('pg1').run;
model.result('pg1').run;
model.result('pg1').set('renderdatacached', true);
model.result.create('pg2', 'PlotGroup2D');
model.result('pg2').run;
model.result.remove('pg2');
model.result('pg1').run;
model.result('pg1').run;
model.result('pg1').feature.create('arws1', 'ArrowSurface');

model.geom('geom1').feature.remove('c2');
model.geom('geom1').run;

model.physics('es').feature.remove('pot1');

model.geom('geom1').run('c1');
model.geom('geom1').feature.create('c2', 'Circle');
model.geom('geom1').feature('c2').set('r', '0.02');
model.geom('geom1').run('c2');
model.geom('geom1').run;

model.physics('es').feature.create('pot1', 'ElectricPotential', 1);

model.geom('geom1').feature('c2').set('createselection', 'on');

model.physics('es').feature('pot1').selection.named('geom1_c2_bnd');
model.physics('es').feature('pot1').set('V0', 1, '150');

model.mesh('mesh1').run;

model.sol('sol1').study('std1');
model.sol('sol1').feature.remove('s1');
model.sol('sol1').feature.remove('v1');
model.sol('sol1').feature.remove('st1');
model.sol('sol1').feature.create('st1', 'StudyStep');
model.sol('sol1').feature('st1').set('study', 'std1');
model.sol('sol1').feature('st1').set('studystep', 'stat');
model.sol('sol1').feature.create('v1', 'Variables');
model.sol('sol1').feature('v1').set('control', 'stat');
model.sol('sol1').feature.create('s1', 'Stationary');
model.sol('sol1').feature('s1').feature.create('fc1', 'FullyCoupled');
model.sol('sol1').feature('s1').feature.remove('fcDef');
model.sol('sol1').attach('std1');
model.sol('sol1').runAll;

model.result('pg1').run;
model.result('pg1').run;
model.result('pg1').run;
model.result('pg1').run;

model.author('Felipe Bandeira da Silva');

model.version('1');

model.comments('Problema 8.7 do Edminster');

out = model;
