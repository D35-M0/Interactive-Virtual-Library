using UnityEngine;
using System.Collections;

public class bookDeform : MonoBehaviour {

    Mesh mesh;

    float lerpTime = 1f;
    float currentTime;

    float moveDistance = .25f;

    Vector3 startPos;
    Vector3 endPos;

	// Use this for initialization
	void Start () {
        mesh = GetComponent<MeshFilter>().mesh;
        startPos = mesh.vertices[0];
        endPos = startPos + transform.up * moveDistance;
	}
	
	// Update is called once per frame
	void Update () {
        currentTime += Time.deltaTime;
        if (currentTime > lerpTime)
        {
            currentTime = lerpTime;
        }

        float perc = currentTime / lerpTime;
        mesh.vertices[0] = Vector3.Lerp(startPos, endPos, perc);
        mesh.RecalculateNormals();
	}
}
