dataset_info = dict(
    dataset_name='animalweb',
    paper_info=dict(
        author='Li, Shuyuan and Li, Jianguo and Tang, Hanlin '
        'and Qian, Rui and Lin, Weiyao',
        title='ATRW: A Benchmark for Amur Tiger '
        'Re-identification in the Wild',
        container='Proceedings of the 28th ACM '
        'International Conference on Multimedia',
        year='2020',
        homepage='https://cvwc2019.github.io/challenge.html',
    ),
    keypoint_info={
        0:
        dict(
            name='left_eye_left',
            id=0,
            color=[51, 153, 255],
            type='upper',
            swap='right_eye_right'),
        1:
        dict(
            name='left_eye_right',
            id=1,
            color=[51, 153, 255],
            type='upper',
            swap='right_eye_left'),
        2:
        dict(
            name='right_eye_left', 
            id=2, color=[51, 153, 255], type='upper', swap='left_eye_right'),
        3:
        dict(
            name='right_eye_right',
            id=3,
            color=[255, 128, 0],
            type='upper',
            swap='left_eye_left'),
        4:
        dict(
            name='nose',
            id=4,
            color=[255, 128, 0],
            type='upper',
            swap=''),
        5:
        dict(
            name='left_mouth',
            id=5,
            color=[0, 255, 0],
            type='lower',
            swap='right_mouth'),
        6:
        dict(
            name='right_mouth',
            id=6,
            color=[0, 255, 0],
            type='lower',
            swap='left_mouth'),
        7:
        dict(
            name='up_mouth',
            id=7,
            color=[255, 128, 0],
            type='lower',
            swap=''),
        8:
        dict(
            name='down_mouth',
            id=8,
            color=[255, 128, 0],
            type='lower',
            swap=''),
        
    },
    skeleton_info={
        
    },
    joint_weights=[1., 1., 1., 1., 1., 1., 1., 1., 1.],
    sigmas=[
        0.025, 0.025, 0.025, 0.025, 0.025, 0.025, 0.025, 0.025, 0.025 
    ])
