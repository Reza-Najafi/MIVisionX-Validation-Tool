__author__      = "Kiriti Nagesh Gowda"
__copyright__   = "Copyright 2019, AMD MIVisionX"
__credits__     = ["Hansel Yang; Lakshmi Kumar;"]
__license__     = "MIT"
__version__     = "0.9.5"
__maintainer__  = "Kiriti Nagesh Gowda"
__email__       = "Kiriti.NageshGowda@amd.com"
__status__      = "ALPHA"
__script_name__ = "MIVisionX Validation Tool"

import sys
#setup python path for RALI
sys.path.append('/opt/rocm/mivisionx/rali/python/')

import os
import argparse
import ctypes
import cv2
import time
import numpy as np
from PyQt4 import QtGui
from inference_control import *

# MIVisionX Classifier
if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	panel = InferenceControl()
	panel.show()
	app.exec_()
	#if len(sys.argv) == 1:
		# modelFormat = (str)(panel.model_format)
		# modelName = (str)(panel.model_name)
		# modelLocation = (str)(panel.model)
		# modelBatchSize = (str)(panel.batch)
		# raliMode = (int)(panel.mode) + 1
		# modelInputDims = (str)(panel.input_dims)
		# modelOutputDims = (str)(panel.output_dims)
		# label = (str)(panel.label)
		# outputDir = (str)(panel.output)
		# imageDir = (str)(panel.image)
		# imageVal = (str)(panel.val)
		# hierarchy = (str)(panel.hier)
		# inputAdd = (str)(panel.add)
		# inputMultiply = (str)(panel.multiply)
		# fp16 = (str)(panel.fp16)
		# replaceModel = (str)(panel.replace)
		# verbose = (str)(panel.verbose)
		# loop = (str)(panel.loop)
		# gui = (str)(panel.gui)
	#else:
		# parser = argparse.ArgumentParser()
		# parser.add_argument('--model_format',		type=str, required=True,	help='pre-trained model format, options:caffe/onnx/nnef [required]')
		# parser.add_argument('--model_name',			type=str, required=True,	help='model name                             [required]')
		# parser.add_argument('--model',				type=str, required=True,	help='pre_trained model file/folder          [required]')
		# parser.add_argument('--model_batch_size',	type=str, required=True,	help='n - batch size			             [required]')
		# parser.add_argument('--rali_mode',			type=str, required=True,	help='rali mode (1/2/3)			             [required]')
		# parser.add_argument('--model_input_dims',	type=str, required=True,	help='c,h,w - channel,height,width           [required]')
		# parser.add_argument('--model_output_dims',	type=str, required=True,	help='c,h,w - channel,height,width           [required]')
		# parser.add_argument('--label',				type=str, required=True,	help='labels text file                       [required]')
		# parser.add_argument('--output_dir',			type=str, required=True,	help='output dir to store ADAT results       [required]')
		# parser.add_argument('--image_dir',			type=str, required=True,	help='image directory for analysis           [required]')
		# parser.add_argument('--image_val',			type=str, default='',		help='image list with ground truth           [optional]')
		# parser.add_argument('--hierarchy',			type=str, default='',		help='AMD proprietary hierarchical file      [optional]')
		# parser.add_argument('--add',				type=str, default='', 		help='input preprocessing factor [optional - default:[0,0,0]]')
		# parser.add_argument('--multiply',			type=str, default='',		help='input preprocessing factor [optional - default:[1,1,1]]')
		# parser.add_argument('--fp16',				type=str, default='no',		help='quantize to FP16 			[optional - default:no]')
		# parser.add_argument('--replace',			type=str, default='no',		help='replace/overwrite model   [optional - default:no]')
		# parser.add_argument('--verbose',			type=str, default='no',		help='verbose                   [optional - default:no]')
		# parser.add_argument('--loop',				type=str, default='yes',	help='verbose                   [optional - default:yes]')
		# parser.add_argument('--gui',				type=str, default='yes',	help='verbose                   [optional - default:yes]')
		# args = parser.parse_args()
		
		# # get arguments
		# modelFormat = args.model_format
		# modelName = args.model_name
		# modelLocation = args.model
		# modelBatchSize = args.model_batch_size
		# raliMode = (int)(args.rali_mode)
		# modelInputDims = args.model_input_dims
		# modelOutputDims = args.model_output_dims
		# label = args.label
		# outputDir = args.output_dir
		# imageDir = args.image_dir
		# imageVal = args.image_val
		# hierarchy = args.hierarchy
		# inputAdd = args.add
		# inputMultiply = args.multiply
		# fp16 = args.fp16
		# replaceModel = args.replace
		# verbose = args.verbose
		# loop = args.loop
		# gui = args.gui

	# # set verbose print
	# if(verbose != 'no'):
	# 	verbosePrint = True

	# # set fp16 inference turned on/off
	# if(fp16 != 'no'):
	# 	FP16inference = True
	# # set paths
	# modelCompilerPath = '/opt/rocm/mivisionx/model_compiler/python'
	# ADATPath= '/opt/rocm/mivisionx/toolkit/analysis_and_visualization/classification'
	# setupDir = '~/.mivisionx-validation-tool'
	# analyzerDir = os.path.expanduser(setupDir)
	# modelDir = analyzerDir+'/'+modelName+'_dir'
	# nnirDir = modelDir+'/nnir-files'
	# openvxDir = modelDir+'/openvx-files'
	# modelBuildDir = modelDir+'/build'
	# adatOutputDir = os.path.expanduser(outputDir)
	# inputImageDir = os.path.expanduser(imageDir)
	# trainedModel = os.path.expanduser(modelLocation)
	# labelText = os.path.expanduser(label)
	# hierarchyText = os.path.expanduser(hierarchy)
	# imageValText = os.path.expanduser(imageVal)
	# pythonLib = modelBuildDir+'/libannpython.so'
	# weightsFile = openvxDir+'/weights.bin'
	# finalImageResultsFile = modelDir+'/imageResultsFile.csv'

	# #set ADAT Flag to generate ADAT only once
	# ADATFlag = False

	# #set GUI Flag
	# guiFlag = False
	# if gui == 'yes':
	# 	guiFlag = True

	# #set loop parameter based on the user input
	# if loop == 'yes':
	# 	loop_parameter = True
	# else:
	# 	loop_parameter = False

	# # get input & output dims
	# str_c_i, str_h_i, str_w_i = modelInputDims.split(',')
	# c_i = int(str_c_i); h_i = int(str_h_i); w_i = int(str_w_i)
	# str_c_o, str_h_o, str_w_o = modelOutputDims.split(',')
	# c_o = int(str_c_o); h_o = int(str_h_o); w_o = int(str_w_o)
	# modelBatchSizeInt = int(modelBatchSize)
	# # input pre-processing values
	# Ax=[0,0,0]
	# if(inputAdd != ''):
	# 	Ax = [float(item) for item in inputAdd.strip("[]").split(',')]
	# Mx=[1,1,1]
	# if(inputMultiply != ''):
	# 	Mx = [float(item) for item in inputMultiply.strip("[]").split(',')]

	# # check pre-trained model
	# if(not os.path.isfile(trainedModel) and modelFormat != 'nnef' ):
	# 	print("\nPre-Trained Model not found, check argument --model\n")
	# 	quit()

	# # check for label file
	# if (not os.path.isfile(labelText)):
	# 	print("\nlabels.txt not found, check argument --label\n")
	# 	quit()
	# else:
	# 	fp = open(labelText, 'r')
	# 	#labelNames = fp.readlines()
	# 	labelNames = [x.strip('\n') for x in fp.readlines()]
	# 	fp.close()

	# # MIVisionX setup
	# if(os.path.exists(analyzerDir)):
	# 	print("\nMIVisionX Validation Tool\n")
	# 	# replace old model or throw error
	# 	if(replaceModel == 'yes'):
	# 		os.system('rm -rf '+modelDir)
	# 	elif(os.path.exists(modelDir)):
	# 		print("OK: Model exists")

	# else:
	# 	print("\nMIVisionX Validation Tool Created\n")
	# 	os.system('(cd ; mkdir .mivisionx-validation-tool)')
	# # Setup Text File for Demo
	# if (not os.path.isfile(analyzerDir + "/setupFile.txt")):
	# 	f = open(analyzerDir + "/setupFile.txt", "w")
	# 	f.write(modelFormat + ';' + modelName + ';' + modelLocation + ';' + modelBatchSize + ';' + modelInputDims + ';' + modelOutputDims + ';' + label + ';' + outputDir + ';' + imageDir + ';' + imageVal + ';' + hierarchy + ';' + str(Ax).strip('[]').replace(" ","") + ';' + str(Mx).strip('[]').replace(" ","") + ';' + fp16 + ';' + replaceModel + ';' + verbose + ';' + loop)
	# 	f.close()
	# else:
	# 	count = len(open(analyzerDir + "/setupFile.txt").readlines())
	# 	if count < 10:
	# 		with open(analyzerDir + "/setupFile.txt", "r") as fin:
	# 			data = fin.read().splitlines(True)
	# 			modelList = []
	# 			for i in range(len(data)):
	# 				if data[i] != '\n':
	# 					modelList.append(data[i].split(';')[1])
	# 			if modelName not in modelList:
	# 				f = open(analyzerDir + "/setupFile.txt", "a")
	# 				f.write("\n" + modelFormat + ';' + modelName + ';' + modelLocation + ';' + modelBatchSize + ';' + modelInputDims + ';' + modelOutputDims + ';' + label + ';' + outputDir + ';' + imageDir + ';' + imageVal + ';' + hierarchy + ';' + str(Ax).strip('[]').replace(" ","") + ';' + str(Mx).strip('[]').replace(" ","") + ';' + fp16 + ';' + replaceModel + ';' + verbose + ';' + loop)
	# 				f.close()
	# 	else:
	# 		with open(analyzerDir + "/setupFile.txt", "r") as fin:
	# 			data = fin.read().splitlines(True)
	# 			delModelName = data[0].split(';')[1]
	# 		delmodelPath = analyzerDir + '/' + delModelName + '_dir'
	# 		if(os.path.exists(delmodelPath)): 
	# 			os.system('rm -rf ' + delmodelPath)
	# 		with open(analyzerDir + "/setupFile.txt", "w") as fout:
	# 		    fout.writelines(data[1:])
	# 		with open(analyzerDir + "/setupFile.txt", "a") as fappend:
	# 			fappend.write("\n" + modelFormat + ';' + modelName + ';' + modelLocation + ';' + modelBatchSize + ';' + modelInputDims + ';' + modelOutputDims + ';' + label + ';' + outputDir + ';' + imageDir + ';' + imageVal + ';' + hierarchy + ';' + str(Ax).strip('[]').replace(" ","") + ';' + str(Mx).strip('[]').replace(" ","") + ';' + fp16 + ';' + replaceModel + ';' + verbose + ';' + loop)
	# 			fappend.close()

	# # Compile Model and generate python .so files
	# if (replaceModel == 'yes' or not os.path.exists(modelDir)):
	# 	os.system('mkdir '+modelDir)
	# 	if(os.path.exists(modelDir)):
	# 		# convert to NNIR
	# 		if(modelFormat == 'caffe'):
	# 			os.system('(cd '+modelDir+'; python '+modelCompilerPath+'/caffe_to_nnir.py '+trainedModel+' nnir-files --input-dims 1,' + modelInputDims + ')')
	# 			os.system('(cd '+modelDir+'; python '+modelCompilerPath+'/nnir_update.py --batch-size ' + modelBatchSize + ' nnir-files nnir-files)')
	# 		elif(modelFormat == 'onnx'):
	# 			os.system('(cd '+modelDir+'; python '+modelCompilerPath+'/onnx_to_nnir.py '+trainedModel+' nnir-files --input_dims 1,' + modelInputDims + ')')
	# 			os.system('(cd '+modelDir+'; python '+modelCompilerPath+'/nnir_update.py --batch-size ' + modelBatchSize + ' nnir-files nnir-files)')
	# 		elif(modelFormat == 'nnef'):
	# 			os.system('(cd '+modelDir+'; python '+modelCompilerPath+'/nnef_to_nnir.py '+trainedModel+' nnir-files --batch-size ' + modelBatchSize + ')')
	# 			#os.system('(cd '+modelDir+'; python '+modelCompilerPath+'/nnir_update.py --batch-size ' + modelBatchSize + ' nnir-files nnir-files)')
	# 		else:
	# 			print("ERROR: Neural Network Format Not supported, use caffe/onnx/nnef in arugment --model_format")
	# 			quit()
	# 		# convert the model to FP16
	# 		if(FP16inference):
	# 			os.system('(cd '+modelDir+'; python '+modelCompilerPath+'/nnir_update.py --convert-fp16 1 --fuse-ops 1 nnir-files nnir-files)')
	# 			print("\nModel Quantized to FP16\n")
	# 		# convert to openvx
	# 		if(os.path.exists(nnirDir)):
	# 			os.system('(cd '+modelDir+'; python '+modelCompilerPath+'/nnir_to_openvx.py nnir-files openvx-files)')
	# 		else:
	# 			print("ERROR: Converting Pre-Trained model to NNIR Failed")
	# 			quit()
			
	# 		# build model
	# 		if(os.path.exists(openvxDir)):
	# 			os.system('mkdir '+modelBuildDir)
	# 		else:
	# 			print("ERROR: Converting NNIR to OpenVX Failed")
	# 			quit()

	# #os.system('(cd '+modelBuildDir+'; cmake ../openvx-files; make; ./anntest ../openvx-files/weights.bin )')
	# print("\nSUCCESS: Converting Pre-Trained model to MIVisionX Runtime successful\n")

	# # create inference classifier
	# classifier = annieObjectWrapper(pythonLib, weightsFile)

	# # check for image val text
	# if(imageVal != ''):
	# 	if (not os.path.isfile(imageValText)):
	# 		print("\nImage Validation Text not found, check argument --image_val\n")
	# 		quit()
	# 	else:
	# 		fp = open(imageValText, 'r')
	# 		imageValidation = fp.readlines()
	# 		fp.close()
	# 		#totalImages = len(imageValidation)
	# else:
	# 	print("\nFlow without Image Validation Text not implemented, pass argument --image_val\n")
	# 	quit()

	# totalImages = len(os.listdir(inputImageDir))
	
	# # original std out location 
	# orig_stdout = sys.stdout
	# # setup results output file
	# sys.stdout = open(finalImageResultsFile,'w')	
	# print('Image File Name,Ground Truth Label,Output Label 1,Output Label 2,Output Label 3,Output Label 4,Output Label 5,Prob 1,Prob 2,Prob 3,Prob 4,Prob 5')
	# sys.stdout = orig_stdout

	# #setup for Rali
	# rali_batch_size = 1
	# start_rali = time.time()
	# loader = DataLoader(inputImageDir, rali_batch_size, modelBatchSizeInt, ColorFormat.IMAGE_RGB24, Affinity.PROCESS_CPU, imageValidation, h_i, w_i, raliMode, loop_parameter)
	# imageIterator = ImageIterator(loader, reverse_channels=False,multiplier=Mx,offset=Ax)
	# raliNumberOfImages = imageIterator.imageCount()
	# end_rali = time.time()
	# if (verbosePrint):
	# 	print '%30s' % 'RALI Data Load Time ', str((end_rali - start_rali)*1000), 'ms'
	# print ('Pipeline created ...')
	# print 'Loader created ...num of images' , loader.getOutputImageCount()
	# print 'Image iterator created ... number of images', raliNumberOfImages

	# #build augmentation list based on RALI mode
	# if modelBatchSizeInt == 16:
	# 	if raliMode == 1:
	# 		raliList = raliList_mode1_16
	# 	elif raliMode == 2:
	# 		raliList = raliList_mode2_16
	# 	elif raliMode == 3:
	# 		raliList = raliList_mode3_16
	# elif modelBatchSizeInt == 64:
	# 	if raliMode == 1:
	# 		raliList = raliList_mode1_64
	# 	elif raliMode == 2:
	# 		raliList = raliList_mode2_64
	# 	elif raliMode == 3:
	# 		raliList = raliList_mode3_64


	# if guiFlag:
	# 	viewer = inference_viewer(modelName, raliMode, totalImages, modelBatchSizeInt)
	# 	viewer.startView()

	#image_tensor has the input tensor required for inference
	# iteratorCount = 0

	# #augmentation intensity
	# augmentation = 0

	# resultPerAugmentation = []

	# for (image_batch, image_tensor) in imageIterator:
	# 	#initialize values for every loop beginning
	# 	x = iteratorCount % raliNumberOfImages
	# 	if x == 0:
	# 		correctTop5 = 0; correctTop1 = 0; wrong = 0; noGroundTruth = 0;
	# 		#create output dict for all the images
	# 		guiResults = {}
	# 		#to calculate FPS
	# 		avg_benchmark = 0.0
	# 		frameMsecs = 0.0
	# 		frameMsecsGUI = 0.0
	# 		totalFPS = 0.0
	# 		del resultPerAugmentation[:]
	# 		for iterator in range(modelBatchSizeInt):
	# 			resultPerAugmentation.append([0,0,0])
	# 		if guiFlag:
	# 			viewer.resetViewer()

	# 	#live updates for augmentaiton slider
	# 	if guiFlag:
	# 		augmentation = viewer.getIntensity()
	# 		loader.updateAugmentationParameter(augmentation)

	# 	msFrame = 0.0
	# 	msFrameGUI = 0.0
	# 	start_main = time.time()

	# 	#get image file name and ground truth
	# 	start = time.time()
	# 	imageFileName = loader.get_input_name()
	# 	groundTruthIndex = loader.get_ground_truth()
	# 	groundTruthIndex = int(groundTruthIndex)
	# 	end = time.time()
	# 	msFrame += (end-start)*1000

	# 	#create output list for each image
	# 	augmentedResults = []

	# 	#create images for display
	# 	start = time.time()
	# 	original_image = image_batch[0:h_i, 0:w_i]
	# 	cloned_image = np.copy(image_batch)
	# 	#using tensor output of RALI as frame
	# 	frame = image_tensor
	# 	end = time.time()
	# 	msFrame += (end - start)*1000
	# 	if(verbosePrint):
	# 		print '%30s' % 'Copying tensor from RALI for inference took ', str((end - start)*1000), 'ms'

	# 	if guiFlag:
	# 		start = time.time()
	# 		groundTruthLabel = labelNames[groundTruthIndex].decode("utf-8").split(' ', 1)
	# 		text_width, text_height = cv2.getTextSize(groundTruthLabel[1].split(',')[0], cv2.FONT_HERSHEY_SIMPLEX, 1.0, 2)[0]
	# 		text_off_x = (w_i/2) - (text_width/2)
	# 		text_off_y = h_i-7
	# 		box_coords = ((text_off_x, text_off_y), (text_off_x + text_width - 2, text_off_y - text_height - 2))
	# 		cv2.rectangle(original_image, box_coords[0], box_coords[1], (245, 197, 66), cv2.FILLED)
	# 		cv2.putText(original_image, groundTruthLabel[1].split(',')[0], (text_off_x, text_off_y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0,0,0), 2)

	# 		#show original image
	# 		width = original_image.shape[1]
	# 		height = original_image.shape[0]
	# 		viewer.showImage(original_image, width, height)
	# 		end = time.time()
	# 		msFrameGUI += (end - start)*1000
	# 		if(verbosePrint):
	# 			print '%30s' % 'Displaying Original Images took ', str((end - start)*1000), 'ms'

	# 	# run inference
	# 	start = time.time()
	# 	output = classifier.classify(frame)
	# 	end = time.time()
	# 	msFrame += (end - start)*1000
	# 	if(verbosePrint):
	# 		print '%30s' % 'Executed Model in ', str((end - start)*1000), 'ms'

	# 	for i in range(loader.getOutputImageCount()):
	# 		# process output and display
	# 		start = time.time()
	# 		topIndex, topProb = processClassificationOutput(frame, modelName, output, modelBatchSizeInt)
	# 		end = time.time()
	# 		msFrame += (end - start)*1000
	# 		if(verbosePrint):
	# 			print '%30s' % 'Processed display in ', str((end - start)*1000), 'ms\n'

	# 		# write image results to a file
	# 		start = time.time()
	# 		sys.stdout = open(finalImageResultsFile,'a')
	# 		print(imageFileName+','+str(groundTruthIndex)+','+str(topIndex[4 + i*4])+
	# 		','+str(topIndex[3 + i*4])+','+str(topIndex[2 + i*4])+','+str(topIndex[1 + i*4])+','+str(topIndex[0 + i*4])+','+str(topProb[4 + i*4])+
	# 		','+str(topProb[3 + i*4])+','+str(topProb[2 + i*4])+','+str(topProb[1 + i*4])+','+str(topProb[0 + i*4]))
	# 		sys.stdout = orig_stdout
	# 		end = time.time()
	# 		msFrame += (end - start)*1000
	# 		if(verbosePrint):
	# 			print '%30s' % 'Image result saved in ', str((end - start)*1000), 'ms'

	# 		start = time.time()
	# 		#data collection for individual augmentation scores
	# 		countPerAugmentation = resultPerAugmentation[i]

	# 		# augmentedResults List: 0 = wrong; 1-5 = TopK; -1 = No Ground Truth
	# 		if(groundTruthIndex == topIndex[4 + i*4]):
	# 			correctTop1 = correctTop1 + 1
	# 			correctTop5 = correctTop5 + 1
	# 			augmentedResults.append(1)
	# 			countPerAugmentation[0] = countPerAugmentation[0] + 1
	# 			countPerAugmentation[1] = countPerAugmentation[1] + 1
	# 		elif(groundTruthIndex == topIndex[3 + i*4] or groundTruthIndex == topIndex[2 + i*4] or groundTruthIndex == topIndex[1 + i*4] or groundTruthIndex == topIndex[0 + i*4]):
	# 			correctTop5 = correctTop5 + 1
	# 			countPerAugmentation[1] = countPerAugmentation[1] + 1
	# 			if (groundTruthIndex == topIndex[3 + i*4]):
	# 				augmentedResults.append(2)
	# 			elif (groundTruthIndex == topIndex[2 + i*4]):
	# 				augmentedResults.append(3)
	# 			elif (groundTruthIndex == topIndex[1 + i*4]):
	# 				augmentedResults.append(4)
	# 			elif (groundTruthIndex == topIndex[0 + i*4]):
	# 				augmentedResults.append(5)
	# 		elif(groundTruthIndex == -1):
	# 			noGroundTruth = noGroundTruth + 1
	# 			augmentedResults.append(-1)
	# 		else:
	# 			wrong = wrong + 1
	# 			augmentedResults.append(0)
	# 			countPerAugmentation[2] = countPerAugmentation[2] + 1

	# 		resultPerAugmentation[i] = countPerAugmentation
	# 		end = time.time()
	# 		msFrame += (end - start)*1000

	# 		if guiFlag:
	# 			augAccuracy = (float)(countPerAugmentation[1]) / (x+1) * 100
	# 			viewer.storeAccuracy(i, augAccuracy)

	# 			start = time.time()
	# 			augmentationText = raliList[i].split('+')
	# 			textCount = len(augmentationText)
	# 			for cnt in range(0,textCount):
	# 				currentText = augmentationText[cnt]
	# 				text_width, text_height = cv2.getTextSize(currentText, cv2.FONT_HERSHEY_SIMPLEX, 1.2, 2)[0]
	# 				text_off_x = (w_i/2) - (text_width/2)
	# 				text_off_y = (i*h_i)+h_i-7-(cnt*text_height)
	# 				box_coords = ((text_off_x, text_off_y), (text_off_x + text_width - 2, text_off_y - text_height - 2))
	# 				cv2.rectangle(cloned_image, box_coords[0], box_coords[1], (245, 197, 66), cv2.FILLED)
	# 				cv2.putText(cloned_image, currentText, (text_off_x, text_off_y), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0,0,0), 2)	

	# 			# put augmented image result
	# 			if augmentedResults[i] == 0:
	# 				cv2.rectangle(cloned_image, (0,(i*(h_i-1)+i)),((w_i-1),(h_i-1)*(i+1) + i), (255,0,0), 4, cv2.LINE_8, 0)
	# 			elif augmentedResults[i] > 0  and augmentedResults[i] < 6:		
	# 				cv2.rectangle(cloned_image, (0,(i*(h_i-1)+i)),((w_i-1),(h_i-1)*(i+1) + i), (0,255,0), 4, cv2.LINE_8, 0)

	# 			end = time.time()
	# 			msFrameGUI += (end - start)*1000
	# 			if(verbosePrint):
	# 				print '%30s' % 'Augmented image results created in ', str((end - start)*1000), 'ms'
		
	# 	if guiFlag:
	# 		#split RALI augmented images into a grid
	# 		start = time.time()
	# 		if modelBatchSizeInt == 64:
	# 			image_batch = np.vsplit(cloned_image, 16)
	# 			final_image_batch = np.hstack((image_batch))
	# 		elif modelBatchSizeInt == 16:
	# 			image_batch = np.vsplit(cloned_image, 4)
	# 			final_image_batch = np.hstack((image_batch))
	# 		end = time.time()
	# 		msFrame += (end - start)*1000
			
	# 		#show augmented images
	# 		start = time.time()
	# 		aug_width = final_image_batch.shape[1]
	# 		aug_height = final_image_batch.shape[0]
	# 		viewer.showAugImage(final_image_batch, aug_width, aug_height)
	# 		#cv2.namedWindow('augmented_images', cv2.WINDOW_GUI_EXPANDED)
	# 		#cv2.imshow('augmented_images', cv2.cvtColor(final_image_batch, cv2.COLOR_RGB2BGR))
	# 		end = time.time()
	# 		msFrameGUI += (end - start)*1000
	# 		if(verbosePrint):
	# 			print '%30s' % 'Displaying Augmented Image took ', str((end - start)*1000), 'ms'

	# 		start = time.time()

	# 		progressIndex = viewer.getIndex()
	# 		if progressIndex == 0:
	# 			viewer.setAugName(modelName)
	# 			# Total progress
	# 			viewer.setTotalProgress((x)*modelBatchSizeInt)
	# 			# Top 1 progress
	# 			viewer.setTop1Progress(correctTop1, x*modelBatchSizeInt)
	# 			# Top 5 progress
	# 			viewer.setTop5Progress(correctTop5, x*modelBatchSizeInt)
	# 			# Mismatch progress
	# 			viewer.setMisProgress(wrong, x*modelBatchSizeInt)
	# 			# No ground truth progress
	# 			#viewer.setNoGTProgress(noGroundTruth)
	# 		else:
	# 			viewer.setAugName(raliList[progressIndex-1])
	# 			# Total progress
	# 			viewer.setTotalProgress(x)
	# 			# Top 1 progress
	# 			viewer.setTop1Progress(resultPerAugmentation[progressIndex-1][0], x)
	# 			# Top 5 progress
	# 			viewer.setTop5Progress(resultPerAugmentation[progressIndex-1][1], x)
	# 			# Mismatch progress
	# 			viewer.setMisProgress(resultPerAugmentation[progressIndex-1][2], x)

	# 		end = time.time()
	# 		msFrameGUI += (end - start)*1000

	# 		if(verbosePrint):
	# 			print '%30s' % 'Progress image created in ', str((end - start)*1000), 'ms'

	# 		# Plot Graph
	# 		start = time.time()
	# 		totalAccuracy = (float)(correctTop5) / (modelBatchSizeInt*x+i+1) * 100
	# 		viewer.plotGraph(totalAccuracy)
	# 		end = time.time()
	# 		msFrameGUI += (end - start)*1000

	# 		# exit inference on ESC; pause/play on SPACEBAR; quit program on 'q'
	# 		key = cv2.waitKey(2)
	# 		if not viewer.getState():
	# 			viewer.stopView()
	# 			break
	# 		while viewer.isPaused():
	# 			cv2.waitKey(0)
	# 			if not viewer.getState():
	# 				break

	# 	guiResults[imageFileName] = augmentedResults
	# 	end_main = time.time()
	# 	if(verbosePrint):
	# 		print '%30s' % 'Process Batch Time ', str((end_main - start_main)*1000), 'ms'
	# 	avg_benchmark += (end_main - start_main)*1000

	# 	#FPS: Inference & Compute
	# 	frameMsecs += msFrame
	# 	frameMsecs = 1000/(frameMsecs/modelBatchSizeInt)
		
	# 	#FPS: GUI
	# 	frameMsecsGUI += msFrameGUI
	# 	frameMsecsGUI = 1000/(frameMsecs/modelBatchSizeInt)

	# 	#FPS: GUI + Inference
	# 	totalFPS += (msFrame + msFrameGUI)
	# 	totalFPS = 1000/(totalFPS/modelBatchSizeInt)

	# 	if guiFlag:
	# 		viewer.displayFPS(totalFPS)
	# 	else:
	# 		if iteratorCount and iteratorCount%5==0:
	# 			#fps text file
	# 			fpsText = open(analyzerDir + "/fps.txt", "w")
	# 			fpsText.write(str(int(frameMsecs)))
	# 			fpsText.close()
	# 			print 'FPS: %d\n' % frameMsecs

	# 	iteratorCount += 1
			
	# 	if ADATFlag == False:
	# 		# Create ADAT folder and file
	# 		print("\nADAT tool called to create the analysis toolkit\n")
	# 		if(not os.path.exists(adatOutputDir)):
	# 			os.system('mkdir ' + adatOutputDir)
			
	# 		if(hierarchy == ''):
	# 			os.system('python '+ADATPath+'/generate-visualization.py --inference_results '+finalImageResultsFile+
	# 			' --image_dir '+inputImageDir+' --label '+labelText+' --model_name '+modelName+' --output_dir '+adatOutputDir+' --output_name '+modelName+'-ADAT')
	# 		else:
	# 			os.system('python '+ADATPath+'/generate-visualization.py --inference_results '+finalImageResultsFile+
	# 			' --image_dir '+inputImageDir+' --label '+labelText+' --hierarchy '+hierarchyText+' --model_name '+modelName+' --output_dir '+adatOutputDir+' --output_name '+modelName+'-ADAT')
	# 		print("\nSUCCESS: Image Analysis Toolkit Created\n")
	# 		if loop == 'no':
	# 			print("Press ESC to exit or close progess window\n")
	# 		ADATFlag = True

	# 	if loop == 'no':
	# 		# Wait to quit
	# 		while True:
	# 			key = cv2.waitKey(2)
	# 			if key == 27:
	# 				cv2.destroyAllWindows()
	# 				break   
	# 			# if cv2.getWindowProperty(windowProgress,cv2.WND_PROP_VISIBLE) < 1:        
	# 			# 	break

	# 	#outputHTMLFile = os.path.expanduser(adatOutputDir+'/'+modelName+'-ADAT-toolKit/index.html')
	# 	#os.system('firefox '+outputHTMLFile)
	
	# if(verbosePrint):
	# 	print '%30s' % 'Average time for one image is ', str(avg_benchmark/raliNumberOfImages), 'ms\n'
	# 	print("\nSUCCESS: Images Inferenced with the Model\n")