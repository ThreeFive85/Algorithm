import Tree from './treeCountLeaves';

describe('treeCountLeaves TEST', () => {
  test('should return a number', (done) => {
    const root = new Tree('root');
    expect(typeof root.countLeaves()).toBe('number');
    done();
  });

  test('should return 1 if the tree root has no children', (done) => {
    const root = new Tree();
    expect(root.countLeaves()).toEqual(1);
    done();
  });

  test('should return 2 if the root has two children', (done) => {
    const root = new Tree();
    root.addChild(new Tree());
    root.addChild(new Tree());

    expect(root.countLeaves()).toEqual(2);
    done();
  });

  test('should still return 2 if one branch has one leaf', (done) => {
    const root = new Tree();
    // add a leaf
    root.addChild(new Tree());
    // add a branch
    const branch = new Tree();
    root.addChild(branch);
    // add a leaf to the branch
    branch.addChild(new Tree());

    // still only two leaves
    expect(root.countLeaves()).toEqual(2);
    done();
  });

  test('should return 4 if both branches have two leaves', (done) => {
    const root = new Tree();
    // add a branch
    const branch1 = new Tree();
    root.addChild(branch1);
    // add two leaves to the branch
    branch1.addChild(new Tree());
    branch1.addChild(new Tree());
    // add another branch
    const branch2 = new Tree();
    root.addChild(branch2);
    // add two leaves to the branch
    branch2.addChild(new Tree());
    branch2.addChild(new Tree());

    // if you're counting, that's four leaves
    expect(root.countLeaves()).toEqual(4);
    done();
  });

  test('should count leaves on a big tree', (done) => {
    // keep a list of nodes by depth to compare
    const root = new Tree();
    // branches
    const branch1 = new Tree();
    const branch2 = new Tree();
    root.addChild(branch1);
    root.addChild(branch2);
    // branches
    const branch3 = new Tree();
    const branch4 = new Tree();
    branch1.addChild(branch2);
    branch1.addChild(branch3);
    // branches
    const branch5 = new Tree();
    const branch6 = new Tree();
    branch3.addChild(branch5);
    branch3.addChild(branch6);

    // leaves
    branch2.addChild(new Tree());
    branch2.addChild(new Tree());
    branch4.addChild(new Tree());
    branch4.addChild(new Tree());
    branch5.addChild(new Tree());
    branch5.addChild(new Tree());
    branch6.addChild(new Tree());
    branch6.addChild(new Tree());

    // so that's eight leaves
    expect(root.countLeaves()).toEqual(8);
    done();
  });
});
