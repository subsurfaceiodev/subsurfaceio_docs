# SubSurface.io

![Logo](https://docs.subsurfaceio.app/assets/logo_vector.svg){ width="300" }
/// caption
SubSurface.io is multipurpose software that automatically estimates
geotechnical, structural, and earthquake engineering parameters.
///

---

**Documentation**: [https://docs.subsurfaceio.app/](https://docs.subsurfaceio.app/){:target="_blank"}

**Package reference**: [subsurfaceio][]

**Web app**: [https://subsurfaceio.app/](https://subsurfaceio.app/){:target="_blank"}

**Interactive API documentation**: [https://www.subsurfaceio.app/docs](https://www.subsurfaceio.app/docs){:target="_blank"}

**Features**: [features.md](features.md)

**Examples**: [examples/api/](examples/api/)

---

## Usage

```python
from subsurfaceio.function_sequences import FunctionSequences

results = FunctionSequences.SoilClassificationUSCS.calculate({
    'language': 'en',
    'fines_content': 34.0,
    'percent_sand': 64.0,
    'percent_gravel': 2.0,
    'liquid_limit': 38.0,
    'plasticity_index': 12.0,
})
```

Runnable scripts live under [Examples](examples/api/index.md). Every public
capability is listed under [Features](features.md). The
[package reference][subsurfaceio] documents every public module.
