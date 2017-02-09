using UnityEngine;
using System.Collections;
using Leap;
using Leap.Unity;
using Leap.Unity.Attributes;

public class SwipeDetector : Detector {


    [Tooltip("The interval in seconds at which to check this detector's conditions.")]
    public float Period = .1f; //seconds

    [AutoFind(AutoFindLocations.Parents)]
    [Tooltip("The hand model to watch. Set automatically if detector is on a hand.")]
    public IHandModel HandModel = null;

    [Tooltip("Reference to a SwipeController to get if hand is swiping or not")]
    public SwipeController controller = null;

    public BookScript book = null;

    private Animator bookAnimator = null;

    private IEnumerator watcherCoroutine;


    private void Awake()
    {
        bookAnimator = book.gameObject.GetComponent<Animator>();
        watcherCoroutine = swipeWatcher();
    }

    private void OnEnable()
    {
        StartCoroutine(watcherCoroutine);
    }

    private void OnDisable()
    {
        StopCoroutine(watcherCoroutine);
        Deactivate();
    }

    private IEnumerator swipeWatcher()
    {
        while (true)
        {

            string layerName = bookAnimator.GetLayerName(0);
            if (controller.IsSwipingLeft && !bookAnimator.GetCurrentAnimatorStateInfo(0).IsName("BaseLayer.Page_Turn"))
            {
                Activate();
            }
            {
                Deactivate();
            }

            yield return new WaitForSeconds(Period);
        }
    }
}
