"""autogenerated by genmsg_py from GetGraspConfigurationsRequest.msg. Do not edit."""
import roslib.message
import struct


class GetGraspConfigurationsRequest(roslib.message.Message):
  _md5sum = "d6a7063359b15cbc8bac77de0a1cc2cb"
  _type = "srs_grasping/GetGraspConfigurationsRequest"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """int32 object_id

"""
  __slots__ = ['object_id']
  _slot_types = ['int32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.
    
    The available fields are:
       object_id
    
    @param args: complete set of field values, in .msg order
    @param kwds: use keyword arguments corresponding to message field names
    to set specific fields. 
    """
    if args or kwds:
      super(GetGraspConfigurationsRequest, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.object_id is None:
        self.object_id = 0
    else:
      self.object_id = 0

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    @param buff: buffer
    @type  buff: StringIO
    """
    try:
      buff.write(_struct_i.pack(self.object_id))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    @param str: byte array of serialized message
    @type  str: str
    """
    try:
      end = 0
      start = end
      end += 4
      (self.object_id,) = _struct_i.unpack(str[start:end])
      return self
    except struct.error as e:
      raise roslib.message.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    @param buff: buffer
    @type  buff: StringIO
    @param numpy: numpy python module
    @type  numpy module
    """
    try:
      buff.write(_struct_i.pack(self.object_id))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    @param str: byte array of serialized message
    @type  str: str
    @param numpy: numpy python module
    @type  numpy: module
    """
    try:
      end = 0
      start = end
      end += 4
      (self.object_id,) = _struct_i.unpack(str[start:end])
      return self
    except struct.error as e:
      raise roslib.message.DeserializationError(e) #most likely buffer underfill

_struct_I = roslib.message.struct_I
_struct_i = struct.Struct("<i")
"""autogenerated by genmsg_py from GetGraspConfigurationsResponse.msg. Do not edit."""
import roslib.message
import struct

import geometry_msgs.msg
import srs_msgs.msg
import std_msgs.msg

class GetGraspConfigurationsResponse(roslib.message.Message):
  _md5sum = "67606ed8cbee8f72e0a708d704b9126f"
  _type = "srs_grasping/GetGraspConfigurationsResponse"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """srs_msgs/GraspConfiguration[] grasp_configuration


================================================================================
MSG: srs_msgs/GraspConfiguration
int32 object_id
string hand_type
float64[] sdh_joint_values
string target_link #link which should be moved to pre_grasp (e.g. sdh_palm_link)
geometry_msgs/PoseStamped pre_grasp
geometry_msgs/PoseStamped grasp
string category

================================================================================
MSG: geometry_msgs/PoseStamped
# A Pose with reference coordinate frame and timestamp
Header header
Pose pose

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.secs: seconds (stamp_secs) since epoch
# * stamp.nsecs: nanoseconds since stamp_secs
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id

================================================================================
MSG: geometry_msgs/Pose
# A representation of pose in free space, composed of postion and orientation. 
Point position
Quaternion orientation

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

================================================================================
MSG: geometry_msgs/Quaternion
# This represents an orientation in free space in quaternion form.

float64 x
float64 y
float64 z
float64 w

"""
  __slots__ = ['grasp_configuration']
  _slot_types = ['srs_msgs/GraspConfiguration[]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.
    
    The available fields are:
       grasp_configuration
    
    @param args: complete set of field values, in .msg order
    @param kwds: use keyword arguments corresponding to message field names
    to set specific fields. 
    """
    if args or kwds:
      super(GetGraspConfigurationsResponse, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.grasp_configuration is None:
        self.grasp_configuration = []
    else:
      self.grasp_configuration = []

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    @param buff: buffer
    @type  buff: StringIO
    """
    try:
      length = len(self.grasp_configuration)
      buff.write(_struct_I.pack(length))
      for val1 in self.grasp_configuration:
        buff.write(_struct_i.pack(val1.object_id))
        _x = val1.hand_type
        length = len(_x)
        buff.write(struct.pack('<I%ss'%length, length, _x))
        length = len(val1.sdh_joint_values)
        buff.write(_struct_I.pack(length))
        pattern = '<%sd'%length
        buff.write(struct.pack(pattern, *val1.sdh_joint_values))
        _x = val1.target_link
        length = len(_x)
        buff.write(struct.pack('<I%ss'%length, length, _x))
        _v1 = val1.pre_grasp
        _v2 = _v1.header
        buff.write(_struct_I.pack(_v2.seq))
        _v3 = _v2.stamp
        _x = _v3
        buff.write(_struct_2I.pack(_x.secs, _x.nsecs))
        _x = _v2.frame_id
        length = len(_x)
        buff.write(struct.pack('<I%ss'%length, length, _x))
        _v4 = _v1.pose
        _v5 = _v4.position
        _x = _v5
        buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
        _v6 = _v4.orientation
        _x = _v6
        buff.write(_struct_4d.pack(_x.x, _x.y, _x.z, _x.w))
        _v7 = val1.grasp
        _v8 = _v7.header
        buff.write(_struct_I.pack(_v8.seq))
        _v9 = _v8.stamp
        _x = _v9
        buff.write(_struct_2I.pack(_x.secs, _x.nsecs))
        _x = _v8.frame_id
        length = len(_x)
        buff.write(struct.pack('<I%ss'%length, length, _x))
        _v10 = _v7.pose
        _v11 = _v10.position
        _x = _v11
        buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
        _v12 = _v10.orientation
        _x = _v12
        buff.write(_struct_4d.pack(_x.x, _x.y, _x.z, _x.w))
        _x = val1.category
        length = len(_x)
        buff.write(struct.pack('<I%ss'%length, length, _x))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    @param str: byte array of serialized message
    @type  str: str
    """
    try:
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.grasp_configuration = []
      for i in range(0, length):
        val1 = srs_msgs.msg.GraspConfiguration()
        start = end
        end += 4
        (val1.object_id,) = _struct_i.unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        val1.hand_type = str[start:end]
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sd'%length
        start = end
        end += struct.calcsize(pattern)
        val1.sdh_joint_values = struct.unpack(pattern, str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        val1.target_link = str[start:end]
        _v13 = val1.pre_grasp
        _v14 = _v13.header
        start = end
        end += 4
        (_v14.seq,) = _struct_I.unpack(str[start:end])
        _v15 = _v14.stamp
        _x = _v15
        start = end
        end += 8
        (_x.secs, _x.nsecs,) = _struct_2I.unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        _v14.frame_id = str[start:end]
        _v16 = _v13.pose
        _v17 = _v16.position
        _x = _v17
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _struct_3d.unpack(str[start:end])
        _v18 = _v16.orientation
        _x = _v18
        start = end
        end += 32
        (_x.x, _x.y, _x.z, _x.w,) = _struct_4d.unpack(str[start:end])
        _v19 = val1.grasp
        _v20 = _v19.header
        start = end
        end += 4
        (_v20.seq,) = _struct_I.unpack(str[start:end])
        _v21 = _v20.stamp
        _x = _v21
        start = end
        end += 8
        (_x.secs, _x.nsecs,) = _struct_2I.unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        _v20.frame_id = str[start:end]
        _v22 = _v19.pose
        _v23 = _v22.position
        _x = _v23
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _struct_3d.unpack(str[start:end])
        _v24 = _v22.orientation
        _x = _v24
        start = end
        end += 32
        (_x.x, _x.y, _x.z, _x.w,) = _struct_4d.unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        val1.category = str[start:end]
        self.grasp_configuration.append(val1)
      return self
    except struct.error as e:
      raise roslib.message.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    @param buff: buffer
    @type  buff: StringIO
    @param numpy: numpy python module
    @type  numpy module
    """
    try:
      length = len(self.grasp_configuration)
      buff.write(_struct_I.pack(length))
      for val1 in self.grasp_configuration:
        buff.write(_struct_i.pack(val1.object_id))
        _x = val1.hand_type
        length = len(_x)
        buff.write(struct.pack('<I%ss'%length, length, _x))
        length = len(val1.sdh_joint_values)
        buff.write(_struct_I.pack(length))
        pattern = '<%sd'%length
        buff.write(val1.sdh_joint_values.tostring())
        _x = val1.target_link
        length = len(_x)
        buff.write(struct.pack('<I%ss'%length, length, _x))
        _v25 = val1.pre_grasp
        _v26 = _v25.header
        buff.write(_struct_I.pack(_v26.seq))
        _v27 = _v26.stamp
        _x = _v27
        buff.write(_struct_2I.pack(_x.secs, _x.nsecs))
        _x = _v26.frame_id
        length = len(_x)
        buff.write(struct.pack('<I%ss'%length, length, _x))
        _v28 = _v25.pose
        _v29 = _v28.position
        _x = _v29
        buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
        _v30 = _v28.orientation
        _x = _v30
        buff.write(_struct_4d.pack(_x.x, _x.y, _x.z, _x.w))
        _v31 = val1.grasp
        _v32 = _v31.header
        buff.write(_struct_I.pack(_v32.seq))
        _v33 = _v32.stamp
        _x = _v33
        buff.write(_struct_2I.pack(_x.secs, _x.nsecs))
        _x = _v32.frame_id
        length = len(_x)
        buff.write(struct.pack('<I%ss'%length, length, _x))
        _v34 = _v31.pose
        _v35 = _v34.position
        _x = _v35
        buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
        _v36 = _v34.orientation
        _x = _v36
        buff.write(_struct_4d.pack(_x.x, _x.y, _x.z, _x.w))
        _x = val1.category
        length = len(_x)
        buff.write(struct.pack('<I%ss'%length, length, _x))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    @param str: byte array of serialized message
    @type  str: str
    @param numpy: numpy python module
    @type  numpy: module
    """
    try:
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.grasp_configuration = []
      for i in range(0, length):
        val1 = srs_msgs.msg.GraspConfiguration()
        start = end
        end += 4
        (val1.object_id,) = _struct_i.unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        val1.hand_type = str[start:end]
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sd'%length
        start = end
        end += struct.calcsize(pattern)
        val1.sdh_joint_values = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        val1.target_link = str[start:end]
        _v37 = val1.pre_grasp
        _v38 = _v37.header
        start = end
        end += 4
        (_v38.seq,) = _struct_I.unpack(str[start:end])
        _v39 = _v38.stamp
        _x = _v39
        start = end
        end += 8
        (_x.secs, _x.nsecs,) = _struct_2I.unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        _v38.frame_id = str[start:end]
        _v40 = _v37.pose
        _v41 = _v40.position
        _x = _v41
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _struct_3d.unpack(str[start:end])
        _v42 = _v40.orientation
        _x = _v42
        start = end
        end += 32
        (_x.x, _x.y, _x.z, _x.w,) = _struct_4d.unpack(str[start:end])
        _v43 = val1.grasp
        _v44 = _v43.header
        start = end
        end += 4
        (_v44.seq,) = _struct_I.unpack(str[start:end])
        _v45 = _v44.stamp
        _x = _v45
        start = end
        end += 8
        (_x.secs, _x.nsecs,) = _struct_2I.unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        _v44.frame_id = str[start:end]
        _v46 = _v43.pose
        _v47 = _v46.position
        _x = _v47
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _struct_3d.unpack(str[start:end])
        _v48 = _v46.orientation
        _x = _v48
        start = end
        end += 32
        (_x.x, _x.y, _x.z, _x.w,) = _struct_4d.unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        val1.category = str[start:end]
        self.grasp_configuration.append(val1)
      return self
    except struct.error as e:
      raise roslib.message.DeserializationError(e) #most likely buffer underfill

_struct_I = roslib.message.struct_I
_struct_i = struct.Struct("<i")
_struct_4d = struct.Struct("<4d")
_struct_2I = struct.Struct("<2I")
_struct_3d = struct.Struct("<3d")
class GetGraspConfigurations(roslib.message.ServiceDefinition):
  _type          = 'srs_grasping/GetGraspConfigurations'
  _md5sum = '37caef0185f2ced87cd79f4e67bb74e0'
  _request_class  = GetGraspConfigurationsRequest
  _response_class = GetGraspConfigurationsResponse
