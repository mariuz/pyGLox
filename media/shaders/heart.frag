uniform float beat;
uniform float time;
varying vec3 normal, lightDir;
varying vec3 vertex, vv;

void main(void)
{
	//vec3 cc = vec3(sin(vertex.z),0,0);
	//cc.y = 0;
	//cc.z = 0;
	
	//vec4 color = vec4(cc,1) * vec4(0.2,0.2,0.2,1) + 0.25;
	vec4 color = vec4(cos(abs(vertex.x)),0,0,1);
	//color.r += cos(beat);
	
	float NdotL = max(dot(normalize(normal), normalize(lightDir)), 0.0);
	if(NdotL > 0.0)
	{
		color += color * NdotL;
		//vec3 hv = normalize(normalize(lightDir) + normalize(vv));
		//color += vec4(cc,1) * pow(max(dot(normalize(normal),hv),0.0),128);
	}
	
	gl_FragColor = color;
}
