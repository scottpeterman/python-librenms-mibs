# SNMP MIB module (INOVONICS-MODEL640-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\inovonics\INOVONICS-MODEL640-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:01:51 2025
# On host DESKTOP-ORUUBP9 platform Windows version 11 by user speterman
# Using Python version 3.12.8 (tags/v3.12.8:2dc476b, Dec  3 2024, 19:30:04) [MSC v.1942 64 bit (AMD64)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 ConstraintsUnion,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "ConstraintsUnion",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint")

# Import SMI symbols from the MIBs this MIB depends on

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 enterprises,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

model640 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 42111, 640)
)
if mibBuilder.loadTexts:
    model640.setRevisions(
        ("2016-02-02 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class OnOff(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )



# MIB Managed Objects in the order of their OIDs

_InovonicsBroadcast_ObjectIdentity = ObjectIdentity
inovonicsBroadcast = _InovonicsBroadcast_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42111)
)
_Traps_ObjectIdentity = ObjectIdentity
traps = _Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42111, 640, 1)
)
_Notifications_ObjectIdentity = ObjectIdentity
notifications = _Notifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42111, 640, 1, 0)
)
_Product_ObjectIdentity = ObjectIdentity
product = _Product_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42111, 640, 2)
)
_Serial_Type = DisplayString
_Serial_Object = MibScalar
serial = _Serial_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 2, 1),
    _Serial_Type()
)
serial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serial.setStatus("current")
_Version_Type = DisplayString
_Version_Object = MibScalar
version = _Version_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 2, 2),
    _Version_Type()
)
version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    version.setStatus("current")
_Date_Type = DisplayString
_Date_Object = MibScalar
date = _Date_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 2, 3),
    _Date_Type()
)
date.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    date.setStatus("current")
_NowPlaying_ObjectIdentity = ObjectIdentity
nowPlaying = _NowPlaying_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42111, 640, 3)
)


class _Frequency_Type(Integer32):
    """Custom type frequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6500, 10800),
    )


_Frequency_Type.__name__ = "Integer32"
_Frequency_Object = MibScalar
frequency = _Frequency_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 3, 1),
    _Frequency_Type()
)
frequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frequency.setStatus("current")


class _CurrentPreset_Type(Integer32):
    """Custom type currentPreset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_CurrentPreset_Type.__name__ = "Integer32"
_CurrentPreset_Object = MibScalar
currentPreset = _CurrentPreset_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 3, 2),
    _CurrentPreset_Type()
)
currentPreset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    currentPreset.setStatus("current")


class _Rssi_Type(Integer32):
    """Custom type rssi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_Rssi_Type.__name__ = "Integer32"
_Rssi_Object = MibScalar
rssi = _Rssi_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 3, 3),
    _Rssi_Type()
)
rssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rssi.setStatus("current")
_Bandwidth_Type = Integer32
_Bandwidth_Object = MibScalar
bandwidth = _Bandwidth_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 3, 4),
    _Bandwidth_Type()
)
bandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandwidth.setStatus("current")


class _Multipath_Type(Integer32):
    """Custom type multipath based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Multipath_Type.__name__ = "Integer32"
_Multipath_Object = MibScalar
multipath = _Multipath_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 3, 5),
    _Multipath_Type()
)
multipath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multipath.setStatus("current")


class _Noise_Type(Integer32):
    """Custom type noise based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Noise_Type.__name__ = "Integer32"
_Noise_Object = MibScalar
noise = _Noise_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 3, 6),
    _Noise_Type()
)
noise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    noise.setStatus("current")


class _LeftLeveldB_Type(Integer32):
    """Custom type leftLeveldB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 6),
    )


_LeftLeveldB_Type.__name__ = "Integer32"
_LeftLeveldB_Object = MibScalar
leftLeveldB = _LeftLeveldB_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 3, 7),
    _LeftLeveldB_Type()
)
leftLeveldB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    leftLeveldB.setStatus("current")


class _RightLeveldB_Type(Integer32):
    """Custom type rightLeveldB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 6),
    )


_RightLeveldB_Type.__name__ = "Integer32"
_RightLeveldB_Object = MibScalar
rightLeveldB = _RightLeveldB_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 3, 8),
    _RightLeveldB_Type()
)
rightLeveldB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rightLeveldB.setStatus("current")


class _LeftPlusRightLeveldB_Type(Integer32):
    """Custom type leftPlusRightLeveldB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 6),
    )


_LeftPlusRightLeveldB_Type.__name__ = "Integer32"
_LeftPlusRightLeveldB_Object = MibScalar
leftPlusRightLeveldB = _LeftPlusRightLeveldB_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 3, 9),
    _LeftPlusRightLeveldB_Type()
)
leftPlusRightLeveldB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    leftPlusRightLeveldB.setStatus("current")


class _LeftMinusRightLeveldB_Type(Integer32):
    """Custom type leftMinusRightLeveldB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 6),
    )


_LeftMinusRightLeveldB_Type.__name__ = "Integer32"
_LeftMinusRightLeveldB_Object = MibScalar
leftMinusRightLeveldB = _LeftMinusRightLeveldB_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 3, 10),
    _LeftMinusRightLeveldB_Type()
)
leftMinusRightLeveldB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    leftMinusRightLeveldB.setStatus("current")
_ReceptionTools_ObjectIdentity = ObjectIdentity
receptionTools = _ReceptionTools_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42111, 640, 4)
)
_BandwidthIF_ObjectIdentity = ObjectIdentity
bandwidthIF = _BandwidthIF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42111, 640, 4, 1)
)


class _BandwidthMode_Type(Integer32):
    """Custom type bandwidthMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("fixed", 0),
          ("auto", 1))
    )


_BandwidthMode_Type.__name__ = "Integer32"
_BandwidthMode_Object = MibScalar
bandwidthMode = _BandwidthMode_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 4, 1, 1),
    _BandwidthMode_Type()
)
bandwidthMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bandwidthMode.setStatus("current")


class _FixedBandwidth_Type(Integer32):
    """Custom type fixedBandwidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("bw56kHz", 0),
          ("bw64kHz", 1),
          ("bw72kHz", 2),
          ("bw84kHz", 3),
          ("bw97kHz", 4),
          ("bw114kHz", 5),
          ("bw133kHz", 6),
          ("bw151kHz", 7),
          ("bw168kHz", 8),
          ("bw184kHz", 9),
          ("bw200kHz", 10),
          ("bw217kHz", 11),
          ("bw236kHz", 12),
          ("bw254kHz", 13),
          ("bw287kHz", 14),
          ("bw311kHz", 15))
    )


_FixedBandwidth_Type.__name__ = "Integer32"
_FixedBandwidth_Object = MibScalar
fixedBandwidth = _FixedBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 4, 1, 2),
    _FixedBandwidth_Type()
)
fixedBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fixedBandwidth.setStatus("current")
_StereoBlend_ObjectIdentity = ObjectIdentity
stereoBlend = _StereoBlend_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42111, 640, 4, 2)
)


class _StereoBlendAmount_Type(Integer32):
    """Custom type stereoBlendAmount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_StereoBlendAmount_Type.__name__ = "Integer32"
_StereoBlendAmount_Object = MibScalar
stereoBlendAmount = _StereoBlendAmount_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 4, 2, 1),
    _StereoBlendAmount_Type()
)
stereoBlendAmount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stereoBlendAmount.setStatus("current")
_StereoBlendAuto_Type = OnOff
_StereoBlendAuto_Object = MibScalar
stereoBlendAuto = _StereoBlendAuto_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 4, 2, 2),
    _StereoBlendAuto_Type()
)
stereoBlendAuto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stereoBlendAuto.setStatus("current")
_StereoBlendUseRSSI_Type = OnOff
_StereoBlendUseRSSI_Object = MibScalar
stereoBlendUseRSSI = _StereoBlendUseRSSI_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 4, 2, 3),
    _StereoBlendUseRSSI_Type()
)
stereoBlendUseRSSI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stereoBlendUseRSSI.setStatus("current")


class _StereoBlendThresholdRSSI_Type(Integer32):
    """Custom type stereoBlendThresholdRSSI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 60),
    )


_StereoBlendThresholdRSSI_Type.__name__ = "Integer32"
_StereoBlendThresholdRSSI_Object = MibScalar
stereoBlendThresholdRSSI = _StereoBlendThresholdRSSI_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 4, 2, 4),
    _StereoBlendThresholdRSSI_Type()
)
stereoBlendThresholdRSSI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stereoBlendThresholdRSSI.setStatus("current")
_StereoBlendUseUSN_Type = OnOff
_StereoBlendUseUSN_Object = MibScalar
stereoBlendUseUSN = _StereoBlendUseUSN_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 4, 2, 5),
    _StereoBlendUseUSN_Type()
)
stereoBlendUseUSN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stereoBlendUseUSN.setStatus("current")


class _StereoBlendThresholdUSN_Type(Integer32):
    """Custom type stereoBlendThresholdUSN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_StereoBlendThresholdUSN_Type.__name__ = "Integer32"
_StereoBlendThresholdUSN_Object = MibScalar
stereoBlendThresholdUSN = _StereoBlendThresholdUSN_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 4, 2, 6),
    _StereoBlendThresholdUSN_Type()
)
stereoBlendThresholdUSN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stereoBlendThresholdUSN.setStatus("current")
_StereoBlendUseMultipath_Type = OnOff
_StereoBlendUseMultipath_Object = MibScalar
stereoBlendUseMultipath = _StereoBlendUseMultipath_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 4, 2, 7),
    _StereoBlendUseMultipath_Type()
)
stereoBlendUseMultipath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stereoBlendUseMultipath.setStatus("current")


class _StereoBlendThresholdMultipath_Type(Integer32):
    """Custom type stereoBlendThresholdMultipath based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_StereoBlendThresholdMultipath_Type.__name__ = "Integer32"
_StereoBlendThresholdMultipath_Object = MibScalar
stereoBlendThresholdMultipath = _StereoBlendThresholdMultipath_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 4, 2, 8),
    _StereoBlendThresholdMultipath_Type()
)
stereoBlendThresholdMultipath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stereoBlendThresholdMultipath.setStatus("current")
_HighBlend_ObjectIdentity = ObjectIdentity
highBlend = _HighBlend_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42111, 640, 4, 3)
)


class _HighBlendAmount_Type(Integer32):
    """Custom type highBlendAmount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HighBlendAmount_Type.__name__ = "Integer32"
_HighBlendAmount_Object = MibScalar
highBlendAmount = _HighBlendAmount_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 4, 3, 1),
    _HighBlendAmount_Type()
)
highBlendAmount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    highBlendAmount.setStatus("current")
_HighBlendAuto_Type = OnOff
_HighBlendAuto_Object = MibScalar
highBlendAuto = _HighBlendAuto_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 4, 3, 2),
    _HighBlendAuto_Type()
)
highBlendAuto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    highBlendAuto.setStatus("current")
_HighBlendUseRSSI_Type = OnOff
_HighBlendUseRSSI_Object = MibScalar
highBlendUseRSSI = _HighBlendUseRSSI_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 4, 3, 3),
    _HighBlendUseRSSI_Type()
)
highBlendUseRSSI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    highBlendUseRSSI.setStatus("current")


class _HighBlendThresholdRSSI_Type(Integer32):
    """Custom type highBlendThresholdRSSI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 60),
    )


_HighBlendThresholdRSSI_Type.__name__ = "Integer32"
_HighBlendThresholdRSSI_Object = MibScalar
highBlendThresholdRSSI = _HighBlendThresholdRSSI_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 4, 3, 4),
    _HighBlendThresholdRSSI_Type()
)
highBlendThresholdRSSI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    highBlendThresholdRSSI.setStatus("current")
_HighBlendUseUSN_Type = OnOff
_HighBlendUseUSN_Object = MibScalar
highBlendUseUSN = _HighBlendUseUSN_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 4, 3, 5),
    _HighBlendUseUSN_Type()
)
highBlendUseUSN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    highBlendUseUSN.setStatus("current")


class _HighBlendThresholdUSN_Type(Integer32):
    """Custom type highBlendThresholdUSN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_HighBlendThresholdUSN_Type.__name__ = "Integer32"
_HighBlendThresholdUSN_Object = MibScalar
highBlendThresholdUSN = _HighBlendThresholdUSN_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 4, 3, 6),
    _HighBlendThresholdUSN_Type()
)
highBlendThresholdUSN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    highBlendThresholdUSN.setStatus("current")
_HighBlendUseMultipath_Type = OnOff
_HighBlendUseMultipath_Object = MibScalar
highBlendUseMultipath = _HighBlendUseMultipath_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 4, 3, 7),
    _HighBlendUseMultipath_Type()
)
highBlendUseMultipath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    highBlendUseMultipath.setStatus("current")


class _HighBlendThresholdMultipath_Type(Integer32):
    """Custom type highBlendThresholdMultipath based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_HighBlendThresholdMultipath_Type.__name__ = "Integer32"
_HighBlendThresholdMultipath_Object = MibScalar
highBlendThresholdMultipath = _HighBlendThresholdMultipath_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 4, 3, 8),
    _HighBlendThresholdMultipath_Type()
)
highBlendThresholdMultipath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    highBlendThresholdMultipath.setStatus("current")
_BandBlend_ObjectIdentity = ObjectIdentity
bandBlend = _BandBlend_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42111, 640, 4, 4)
)
_BandBlendEnable_Type = OnOff
_BandBlendEnable_Object = MibScalar
bandBlendEnable = _BandBlendEnable_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 4, 4, 1),
    _BandBlendEnable_Type()
)
bandBlendEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bandBlendEnable.setStatus("current")


class _BandBlendControl_Type(Integer32):
    """Custom type bandBlendControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 150),
    )


_BandBlendControl_Type.__name__ = "Integer32"
_BandBlendControl_Object = MibScalar
bandBlendControl = _BandBlendControl_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 4, 4, 2),
    _BandBlendControl_Type()
)
bandBlendControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bandBlendControl.setStatus("current")


class _BandBlendLF_Type(Integer32):
    """Custom type bandBlendLF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_BandBlendLF_Type.__name__ = "Integer32"
_BandBlendLF_Object = MibScalar
bandBlendLF = _BandBlendLF_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 4, 4, 3),
    _BandBlendLF_Type()
)
bandBlendLF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandBlendLF.setStatus("current")


class _BandBlend2k_Type(Integer32):
    """Custom type bandBlend2k based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_BandBlend2k_Type.__name__ = "Integer32"
_BandBlend2k_Object = MibScalar
bandBlend2k = _BandBlend2k_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 4, 4, 4),
    _BandBlend2k_Type()
)
bandBlend2k.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandBlend2k.setStatus("current")


class _BandBlend5k_Type(Integer32):
    """Custom type bandBlend5k based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_BandBlend5k_Type.__name__ = "Integer32"
_BandBlend5k_Object = MibScalar
bandBlend5k = _BandBlend5k_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 4, 4, 5),
    _BandBlend5k_Type()
)
bandBlend5k.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandBlend5k.setStatus("current")


class _BandBlendHF_Type(Integer32):
    """Custom type bandBlendHF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_BandBlendHF_Type.__name__ = "Integer32"
_BandBlendHF_Object = MibScalar
bandBlendHF = _BandBlendHF_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 4, 4, 6),
    _BandBlendHF_Type()
)
bandBlendHF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandBlendHF.setStatus("current")
_Highcut_ObjectIdentity = ObjectIdentity
highcut = _Highcut_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42111, 640, 4, 5)
)


class _HighcutAmount_Type(Integer32):
    """Custom type highcutAmount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HighcutAmount_Type.__name__ = "Integer32"
_HighcutAmount_Object = MibScalar
highcutAmount = _HighcutAmount_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 4, 5, 1),
    _HighcutAmount_Type()
)
highcutAmount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    highcutAmount.setStatus("current")
_HighcutAuto_Type = OnOff
_HighcutAuto_Object = MibScalar
highcutAuto = _HighcutAuto_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 4, 5, 2),
    _HighcutAuto_Type()
)
highcutAuto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    highcutAuto.setStatus("current")
_HighcutUseRSSI_Type = OnOff
_HighcutUseRSSI_Object = MibScalar
highcutUseRSSI = _HighcutUseRSSI_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 4, 5, 3),
    _HighcutUseRSSI_Type()
)
highcutUseRSSI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    highcutUseRSSI.setStatus("current")


class _HighcutThresholdRSSI_Type(Integer32):
    """Custom type highcutThresholdRSSI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 60),
    )


_HighcutThresholdRSSI_Type.__name__ = "Integer32"
_HighcutThresholdRSSI_Object = MibScalar
highcutThresholdRSSI = _HighcutThresholdRSSI_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 4, 5, 4),
    _HighcutThresholdRSSI_Type()
)
highcutThresholdRSSI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    highcutThresholdRSSI.setStatus("current")
_HighcutUseUSN_Type = OnOff
_HighcutUseUSN_Object = MibScalar
highcutUseUSN = _HighcutUseUSN_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 4, 5, 5),
    _HighcutUseUSN_Type()
)
highcutUseUSN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    highcutUseUSN.setStatus("current")


class _HighcutThresholdUSN_Type(Integer32):
    """Custom type highcutThresholdUSN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_HighcutThresholdUSN_Type.__name__ = "Integer32"
_HighcutThresholdUSN_Object = MibScalar
highcutThresholdUSN = _HighcutThresholdUSN_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 4, 5, 6),
    _HighcutThresholdUSN_Type()
)
highcutThresholdUSN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    highcutThresholdUSN.setStatus("current")
_HighcutUseMultipath_Type = OnOff
_HighcutUseMultipath_Object = MibScalar
highcutUseMultipath = _HighcutUseMultipath_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 4, 5, 7),
    _HighcutUseMultipath_Type()
)
highcutUseMultipath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    highcutUseMultipath.setStatus("current")


class _HighcutThresholdMultipath_Type(Integer32):
    """Custom type highcutThresholdMultipath based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_HighcutThresholdMultipath_Type.__name__ = "Integer32"
_HighcutThresholdMultipath_Object = MibScalar
highcutThresholdMultipath = _HighcutThresholdMultipath_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 4, 5, 8),
    _HighcutThresholdMultipath_Type()
)
highcutThresholdMultipath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    highcutThresholdMultipath.setStatus("current")


class _MonoStereo_Type(Integer32):
    """Custom type monoStereo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("forcedMono", 0),
          ("stereo", 1))
    )


_MonoStereo_Type.__name__ = "Integer32"
_MonoStereo_Object = MibScalar
monoStereo = _MonoStereo_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 4, 6),
    _MonoStereo_Type()
)
monoStereo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    monoStereo.setStatus("current")
_MultipathSuppression_Type = OnOff
_MultipathSuppression_Object = MibScalar
multipathSuppression = _MultipathSuppression_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 4, 7),
    _MultipathSuppression_Type()
)
multipathSuppression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    multipathSuppression.setStatus("current")
_ChannelEqualizer_Type = OnOff
_ChannelEqualizer_Object = MibScalar
channelEqualizer = _ChannelEqualizer_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 4, 8),
    _ChannelEqualizer_Type()
)
channelEqualizer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    channelEqualizer.setStatus("current")
_Rds_ObjectIdentity = ObjectIdentity
rds = _Rds_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42111, 640, 5)
)
_Pi_Type = DisplayString
_Pi_Object = MibScalar
pi = _Pi_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 5, 1),
    _Pi_Type()
)
pi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pi.setStatus("current")
_Call_Type = DisplayString
_Call_Object = MibScalar
call = _Call_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 5, 2),
    _Call_Type()
)
call.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    call.setStatus("current")
_Ps_Type = DisplayString
_Ps_Object = MibScalar
ps = _Ps_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 5, 3),
    _Ps_Type()
)
ps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ps.setStatus("current")
_Rt_Type = DisplayString
_Rt_Object = MibScalar
rt = _Rt_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 5, 4),
    _Rt_Type()
)
rt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rt.setStatus("current")
_Pty_Type = DisplayString
_Pty_Object = MibScalar
pty = _Pty_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 5, 5),
    _Pty_Type()
)
pty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pty.setStatus("current")
_Ptyn_Type = DisplayString
_Ptyn_Object = MibScalar
ptyn = _Ptyn_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 5, 6),
    _Ptyn_Type()
)
ptyn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptyn.setStatus("current")
_RdsTime_Type = DisplayString
_RdsTime_Object = MibScalar
rdsTime = _RdsTime_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 5, 7),
    _RdsTime_Type()
)
rdsTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdsTime.setStatus("current")


class _Ms_Type(Integer32):
    """Custom type ms based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("speech", 0),
          ("music", 1))
    )


_Ms_Type.__name__ = "Integer32"
_Ms_Object = MibScalar
ms = _Ms_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 5, 8),
    _Ms_Type()
)
ms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ms.setStatus("current")


class _Di_Type(Integer32):
    """Custom type di based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("mono", 0),
          ("stereo", 1))
    )


_Di_Type.__name__ = "Integer32"
_Di_Object = MibScalar
di = _Di_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 5, 9),
    _Di_Type()
)
di.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    di.setStatus("current")


class _Tp_Type(Integer32):
    """Custom type tp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Tp_Type.__name__ = "Integer32"
_Tp_Object = MibScalar
tp = _Tp_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 5, 10),
    _Tp_Type()
)
tp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tp.setStatus("current")
_Ta_Type = OnOff
_Ta_Object = MibScalar
ta = _Ta_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 5, 11),
    _Ta_Type()
)
ta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ta.setStatus("current")
_Alarms_ObjectIdentity = ObjectIdentity
alarms = _Alarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42111, 640, 6)
)
_AlarmStatus_ObjectIdentity = ObjectIdentity
alarmStatus = _AlarmStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42111, 640, 6, 1)
)
_AudioLossAlarm_Type = OnOff
_AudioLossAlarm_Object = MibScalar
audioLossAlarm = _AudioLossAlarm_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 6, 1, 1),
    _AudioLossAlarm_Type()
)
audioLossAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    audioLossAlarm.setStatus("current")
_LowSignalAlarm_Type = OnOff
_LowSignalAlarm_Object = MibScalar
lowSignalAlarm = _LowSignalAlarm_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 6, 1, 2),
    _LowSignalAlarm_Type()
)
lowSignalAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lowSignalAlarm.setStatus("current")
_RdsErrorAlarm_Type = OnOff
_RdsErrorAlarm_Object = MibScalar
rdsErrorAlarm = _RdsErrorAlarm_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 6, 1, 3),
    _RdsErrorAlarm_Type()
)
rdsErrorAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdsErrorAlarm.setStatus("current")
_PilotLossAlarm_Type = OnOff
_PilotLossAlarm_Object = MibScalar
pilotLossAlarm = _PilotLossAlarm_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 6, 1, 4),
    _PilotLossAlarm_Type()
)
pilotLossAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pilotLossAlarm.setStatus("current")
_AudioLoss_ObjectIdentity = ObjectIdentity
audioLoss = _AudioLoss_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42111, 640, 6, 2)
)
_AudioLossEnable_Type = OnOff
_AudioLossEnable_Object = MibScalar
audioLossEnable = _AudioLossEnable_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 6, 2, 1),
    _AudioLossEnable_Type()
)
audioLossEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    audioLossEnable.setStatus("current")


class _AudioLossThreshOn_Type(Integer32):
    """Custom type audioLossThreshOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-40, 0),
    )


_AudioLossThreshOn_Type.__name__ = "Integer32"
_AudioLossThreshOn_Object = MibScalar
audioLossThreshOn = _AudioLossThreshOn_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 6, 2, 2),
    _AudioLossThreshOn_Type()
)
audioLossThreshOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    audioLossThreshOn.setStatus("current")


class _AudioLossThreshOff_Type(Integer32):
    """Custom type audioLossThreshOff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-40, 0),
    )


_AudioLossThreshOff_Type.__name__ = "Integer32"
_AudioLossThreshOff_Object = MibScalar
audioLossThreshOff = _AudioLossThreshOff_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 6, 2, 3),
    _AudioLossThreshOff_Type()
)
audioLossThreshOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    audioLossThreshOff.setStatus("current")


class _AudioLossTimeOn_Type(Integer32):
    """Custom type audioLossTimeOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_AudioLossTimeOn_Type.__name__ = "Integer32"
_AudioLossTimeOn_Object = MibScalar
audioLossTimeOn = _AudioLossTimeOn_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 6, 2, 4),
    _AudioLossTimeOn_Type()
)
audioLossTimeOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    audioLossTimeOn.setStatus("current")


class _AudioLossTimeOff_Type(Integer32):
    """Custom type audioLossTimeOff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_AudioLossTimeOff_Type.__name__ = "Integer32"
_AudioLossTimeOff_Object = MibScalar
audioLossTimeOff = _AudioLossTimeOff_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 6, 2, 5),
    _AudioLossTimeOff_Type()
)
audioLossTimeOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    audioLossTimeOff.setStatus("current")
_LowSignal_ObjectIdentity = ObjectIdentity
lowSignal = _LowSignal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42111, 640, 6, 3)
)
_LowSignalEnable_Type = OnOff
_LowSignalEnable_Object = MibScalar
lowSignalEnable = _LowSignalEnable_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 6, 3, 1),
    _LowSignalEnable_Type()
)
lowSignalEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lowSignalEnable.setStatus("current")
_LowSignalMute_Type = OnOff
_LowSignalMute_Object = MibScalar
lowSignalMute = _LowSignalMute_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 6, 3, 2),
    _LowSignalMute_Type()
)
lowSignalMute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lowSignalMute.setStatus("current")


class _LowSignalThreshOn_Type(Integer32):
    """Custom type lowSignalThreshOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 80),
    )


_LowSignalThreshOn_Type.__name__ = "Integer32"
_LowSignalThreshOn_Object = MibScalar
lowSignalThreshOn = _LowSignalThreshOn_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 6, 3, 3),
    _LowSignalThreshOn_Type()
)
lowSignalThreshOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lowSignalThreshOn.setStatus("current")


class _LowSignalThreshOff_Type(Integer32):
    """Custom type lowSignalThreshOff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 80),
    )


_LowSignalThreshOff_Type.__name__ = "Integer32"
_LowSignalThreshOff_Object = MibScalar
lowSignalThreshOff = _LowSignalThreshOff_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 6, 3, 4),
    _LowSignalThreshOff_Type()
)
lowSignalThreshOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lowSignalThreshOff.setStatus("current")


class _LowSignalTimeOn_Type(Integer32):
    """Custom type lowSignalTimeOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_LowSignalTimeOn_Type.__name__ = "Integer32"
_LowSignalTimeOn_Object = MibScalar
lowSignalTimeOn = _LowSignalTimeOn_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 6, 3, 5),
    _LowSignalTimeOn_Type()
)
lowSignalTimeOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lowSignalTimeOn.setStatus("current")


class _LowSignalTimeOff_Type(Integer32):
    """Custom type lowSignalTimeOff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_LowSignalTimeOff_Type.__name__ = "Integer32"
_LowSignalTimeOff_Object = MibScalar
lowSignalTimeOff = _LowSignalTimeOff_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 6, 3, 6),
    _LowSignalTimeOff_Type()
)
lowSignalTimeOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lowSignalTimeOff.setStatus("current")
_RdsLoss_ObjectIdentity = ObjectIdentity
rdsLoss = _RdsLoss_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42111, 640, 6, 4)
)
_RdsLossEnable_Type = OnOff
_RdsLossEnable_Object = MibScalar
rdsLossEnable = _RdsLossEnable_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 6, 4, 1),
    _RdsLossEnable_Type()
)
rdsLossEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdsLossEnable.setStatus("current")
_RdsPIErrorEnable_Type = OnOff
_RdsPIErrorEnable_Object = MibScalar
rdsPIErrorEnable = _RdsPIErrorEnable_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 6, 4, 2),
    _RdsPIErrorEnable_Type()
)
rdsPIErrorEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdsPIErrorEnable.setStatus("current")


class _RdsPICode_Type(DisplayString):
    """Custom type rdsPICode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_RdsPICode_Type.__name__ = "DisplayString"
_RdsPICode_Object = MibScalar
rdsPICode = _RdsPICode_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 6, 4, 3),
    _RdsPICode_Type()
)
rdsPICode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdsPICode.setStatus("current")


class _RdsLossTimeOn_Type(Integer32):
    """Custom type rdsLossTimeOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_RdsLossTimeOn_Type.__name__ = "Integer32"
_RdsLossTimeOn_Object = MibScalar
rdsLossTimeOn = _RdsLossTimeOn_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 6, 4, 4),
    _RdsLossTimeOn_Type()
)
rdsLossTimeOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdsLossTimeOn.setStatus("current")


class _RdsLossTimeOff_Type(Integer32):
    """Custom type rdsLossTimeOff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_RdsLossTimeOff_Type.__name__ = "Integer32"
_RdsLossTimeOff_Object = MibScalar
rdsLossTimeOff = _RdsLossTimeOff_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 6, 4, 5),
    _RdsLossTimeOff_Type()
)
rdsLossTimeOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdsLossTimeOff.setStatus("current")
_PilotLoss_ObjectIdentity = ObjectIdentity
pilotLoss = _PilotLoss_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42111, 640, 6, 5)
)
_PilotLossEnable_Type = OnOff
_PilotLossEnable_Object = MibScalar
pilotLossEnable = _PilotLossEnable_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 6, 5, 1),
    _PilotLossEnable_Type()
)
pilotLossEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pilotLossEnable.setStatus("current")


class _PilotLossTimeOn_Type(Integer32):
    """Custom type pilotLossTimeOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_PilotLossTimeOn_Type.__name__ = "Integer32"
_PilotLossTimeOn_Object = MibScalar
pilotLossTimeOn = _PilotLossTimeOn_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 6, 5, 2),
    _PilotLossTimeOn_Type()
)
pilotLossTimeOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pilotLossTimeOn.setStatus("current")


class _PilotLossTimeOff_Type(Integer32):
    """Custom type pilotLossTimeOff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_PilotLossTimeOff_Type.__name__ = "Integer32"
_PilotLossTimeOff_Object = MibScalar
pilotLossTimeOff = _PilotLossTimeOff_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 6, 5, 3),
    _PilotLossTimeOff_Type()
)
pilotLossTimeOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pilotLossTimeOff.setStatus("current")
_Setup_ObjectIdentity = ObjectIdentity
setup = _Setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42111, 640, 7)
)
_Outputs_ObjectIdentity = ObjectIdentity
outputs = _Outputs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42111, 640, 7, 1)
)


class _AnalogLevel_Type(Integer32):
    """Custom type analogLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-200, 180),
    )


_AnalogLevel_Type.__name__ = "Integer32"
_AnalogLevel_Object = MibScalar
analogLevel = _AnalogLevel_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 7, 1, 1),
    _AnalogLevel_Type()
)
analogLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    analogLevel.setStatus("current")
_AnalogDeemphasis_Type = OnOff
_AnalogDeemphasis_Object = MibScalar
analogDeemphasis = _AnalogDeemphasis_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 7, 1, 2),
    _AnalogDeemphasis_Type()
)
analogDeemphasis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    analogDeemphasis.setStatus("current")


class _DigitalLevel_Type(Integer32):
    """Custom type digitalLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-300, 0),
    )


_DigitalLevel_Type.__name__ = "Integer32"
_DigitalLevel_Object = MibScalar
digitalLevel = _DigitalLevel_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 7, 1, 3),
    _DigitalLevel_Type()
)
digitalLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digitalLevel.setStatus("current")
_DigitalDeemphasis_Type = OnOff
_DigitalDeemphasis_Object = MibScalar
digitalDeemphasis = _DigitalDeemphasis_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 7, 1, 4),
    _DigitalDeemphasis_Type()
)
digitalDeemphasis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digitalDeemphasis.setStatus("current")


class _MpxLevel_Type(Integer32):
    """Custom type mpxLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 6000),
    )


_MpxLevel_Type.__name__ = "Integer32"
_MpxLevel_Object = MibScalar
mpxLevel = _MpxLevel_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 7, 1, 5),
    _MpxLevel_Type()
)
mpxLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpxLevel.setStatus("current")


class _MpxClipping_Type(Integer32):
    """Custom type mpxClipping based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-20, 30),
    )


_MpxClipping_Type.__name__ = "Integer32"
_MpxClipping_Object = MibScalar
mpxClipping = _MpxClipping_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 7, 1, 6),
    _MpxClipping_Type()
)
mpxClipping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpxClipping.setStatus("current")
_Network_ObjectIdentity = ObjectIdentity
network = _Network_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42111, 640, 7, 2)
)


class _Dhcp_Type(Integer32):
    """Custom type dhcp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("staticIP", 0),
          ("dhcpEnabled", 1))
    )


_Dhcp_Type.__name__ = "Integer32"
_Dhcp_Object = MibScalar
dhcp = _Dhcp_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 7, 2, 1),
    _Dhcp_Type()
)
dhcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcp.setStatus("current")
_Ip_Type = IpAddress
_Ip_Object = MibScalar
ip = _Ip_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 7, 2, 2),
    _Ip_Type()
)
ip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ip.setStatus("current")
_Gateway_Type = IpAddress
_Gateway_Object = MibScalar
gateway = _Gateway_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 7, 2, 3),
    _Gateway_Type()
)
gateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gateway.setStatus("current")
_Subnet_Type = IpAddress
_Subnet_Object = MibScalar
subnet = _Subnet_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 7, 2, 4),
    _Subnet_Type()
)
subnet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subnet.setStatus("current")
_Dns_Type = IpAddress
_Dns_Object = MibScalar
dns = _Dns_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 7, 2, 5),
    _Dns_Type()
)
dns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dns.setStatus("current")


class _HttpPort_Type(Integer32):
    """Custom type httpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HttpPort_Type.__name__ = "Integer32"
_HttpPort_Object = MibScalar
httpPort = _HttpPort_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 7, 2, 6),
    _HttpPort_Type()
)
httpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    httpPort.setStatus("current")


class _Hostname_Type(DisplayString):
    """Custom type hostname based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Hostname_Type.__name__ = "DisplayString"
_Hostname_Object = MibScalar
hostname = _Hostname_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 7, 2, 7),
    _Hostname_Type()
)
hostname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hostname.setStatus("current")
_Mac_Type = DisplayString
_Mac_Object = MibScalar
mac = _Mac_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 7, 2, 8),
    _Mac_Type()
)
mac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mac.setStatus("current")
_DynDNS_ObjectIdentity = ObjectIdentity
dynDNS = _DynDNS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42111, 640, 7, 3)
)


class _DdnsMode_Type(Integer32):
    """Custom type ddnsMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("dyn", 1),
          ("noip", 2),
          ("dnsomatic", 3))
    )


_DdnsMode_Type.__name__ = "Integer32"
_DdnsMode_Object = MibScalar
ddnsMode = _DdnsMode_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 7, 3, 1),
    _DdnsMode_Type()
)
ddnsMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ddnsMode.setStatus("current")


class _DdnsHostname_Type(DisplayString):
    """Custom type ddnsHostname based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_DdnsHostname_Type.__name__ = "DisplayString"
_DdnsHostname_Object = MibScalar
ddnsHostname = _DdnsHostname_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 7, 3, 2),
    _DdnsHostname_Type()
)
ddnsHostname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ddnsHostname.setStatus("current")


class _DdnsUsername_Type(DisplayString):
    """Custom type ddnsUsername based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_DdnsUsername_Type.__name__ = "DisplayString"
_DdnsUsername_Object = MibScalar
ddnsUsername = _DdnsUsername_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 7, 3, 3),
    _DdnsUsername_Type()
)
ddnsUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ddnsUsername.setStatus("current")


class _DdnsPassword_Type(DisplayString):
    """Custom type ddnsPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_DdnsPassword_Type.__name__ = "DisplayString"
_DdnsPassword_Object = MibScalar
ddnsPassword = _DdnsPassword_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 7, 3, 4),
    _DdnsPassword_Type()
)
ddnsPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ddnsPassword.setStatus("current")
_DdnsStatus_Type = DisplayString
_DdnsStatus_Object = MibScalar
ddnsStatus = _DdnsStatus_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 7, 3, 5),
    _DdnsStatus_Type()
)
ddnsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddnsStatus.setStatus("current")
_Time_ObjectIdentity = ObjectIdentity
time = _Time_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42111, 640, 7, 4)
)


class _Timezone_Type(Integer32):
    """Custom type timezone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-120, 140),
    )


_Timezone_Type.__name__ = "Integer32"
_Timezone_Object = MibScalar
timezone = _Timezone_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 7, 4, 1),
    _Timezone_Type()
)
timezone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timezone.setStatus("current")
_Dst_Type = OnOff
_Dst_Object = MibScalar
dst = _Dst_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 7, 4, 2),
    _Dst_Type()
)
dst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dst.setStatus("current")
_Autodst_Type = OnOff
_Autodst_Object = MibScalar
autodst = _Autodst_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 7, 4, 3),
    _Autodst_Type()
)
autodst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autodst.setStatus("current")


class _TimeServer_Type(DisplayString):
    """Custom type timeServer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_TimeServer_Type.__name__ = "DisplayString"
_TimeServer_Object = MibScalar
timeServer = _TimeServer_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 7, 4, 4),
    _TimeServer_Type()
)
timeServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeServer.setStatus("current")
_Snmp_ObjectIdentity = ObjectIdentity
snmp = _Snmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42111, 640, 7, 5)
)


class _SnmpMode_Type(Integer32):
    """Custom type snmpMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("readOnly", 1),
          ("readWrite", 2))
    )


_SnmpMode_Type.__name__ = "Integer32"
_SnmpMode_Object = MibScalar
snmpMode = _SnmpMode_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 7, 5, 1),
    _SnmpMode_Type()
)
snmpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpMode.setStatus("current")


class _SnmpReadCommunity_Type(DisplayString):
    """Custom type snmpReadCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_SnmpReadCommunity_Type.__name__ = "DisplayString"
_SnmpReadCommunity_Object = MibScalar
snmpReadCommunity = _SnmpReadCommunity_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 7, 5, 2),
    _SnmpReadCommunity_Type()
)
snmpReadCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpReadCommunity.setStatus("current")


class _SnmpWriteCommunity_Type(DisplayString):
    """Custom type snmpWriteCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_SnmpWriteCommunity_Type.__name__ = "DisplayString"
_SnmpWriteCommunity_Object = MibScalar
snmpWriteCommunity = _SnmpWriteCommunity_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 7, 5, 3),
    _SnmpWriteCommunity_Type()
)
snmpWriteCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpWriteCommunity.setStatus("current")


class _SnmpPort_Type(Integer32):
    """Custom type snmpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SnmpPort_Type.__name__ = "Integer32"
_SnmpPort_Object = MibScalar
snmpPort = _SnmpPort_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 7, 5, 4),
    _SnmpPort_Type()
)
snmpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpPort.setStatus("current")


class _SnmpTrapsPort_Type(Integer32):
    """Custom type snmpTrapsPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SnmpTrapsPort_Type.__name__ = "Integer32"
_SnmpTrapsPort_Object = MibScalar
snmpTrapsPort = _SnmpTrapsPort_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 7, 5, 5),
    _SnmpTrapsPort_Type()
)
snmpTrapsPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapsPort.setStatus("current")
_SnmpTrapDestination1_Type = IpAddress
_SnmpTrapDestination1_Object = MibScalar
snmpTrapDestination1 = _SnmpTrapDestination1_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 7, 5, 6),
    _SnmpTrapDestination1_Type()
)
snmpTrapDestination1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapDestination1.setStatus("current")
_SnmpTrapDestination2_Type = IpAddress
_SnmpTrapDestination2_Object = MibScalar
snmpTrapDestination2 = _SnmpTrapDestination2_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 7, 5, 7),
    _SnmpTrapDestination2_Type()
)
snmpTrapDestination2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapDestination2.setStatus("current")
_SnmpTrapDestination3_Type = IpAddress
_SnmpTrapDestination3_Object = MibScalar
snmpTrapDestination3 = _SnmpTrapDestination3_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 7, 5, 8),
    _SnmpTrapDestination3_Type()
)
snmpTrapDestination3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapDestination3.setStatus("current")
_Email_ObjectIdentity = ObjectIdentity
email = _Email_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42111, 640, 7, 6)
)


class _SmtpServer_Type(DisplayString):
    """Custom type smtpServer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_SmtpServer_Type.__name__ = "DisplayString"
_SmtpServer_Object = MibScalar
smtpServer = _SmtpServer_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 7, 6, 1),
    _SmtpServer_Type()
)
smtpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smtpServer.setStatus("current")


class _SmtpPort_Type(Integer32):
    """Custom type smtpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SmtpPort_Type.__name__ = "Integer32"
_SmtpPort_Object = MibScalar
smtpPort = _SmtpPort_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 7, 6, 2),
    _SmtpPort_Type()
)
smtpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smtpPort.setStatus("current")
_Ssl_Type = OnOff
_Ssl_Object = MibScalar
ssl = _Ssl_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 7, 6, 3),
    _Ssl_Type()
)
ssl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ssl.setStatus("current")


class _EmailFrom_Type(DisplayString):
    """Custom type emailFrom based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_EmailFrom_Type.__name__ = "DisplayString"
_EmailFrom_Object = MibScalar
emailFrom = _EmailFrom_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 7, 6, 4),
    _EmailFrom_Type()
)
emailFrom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailFrom.setStatus("current")


class _EmailUsername_Type(DisplayString):
    """Custom type emailUsername based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_EmailUsername_Type.__name__ = "DisplayString"
_EmailUsername_Object = MibScalar
emailUsername = _EmailUsername_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 7, 6, 5),
    _EmailUsername_Type()
)
emailUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailUsername.setStatus("current")


class _EmailPassword_Type(DisplayString):
    """Custom type emailPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_EmailPassword_Type.__name__ = "DisplayString"
_EmailPassword_Object = MibScalar
emailPassword = _EmailPassword_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 7, 6, 6),
    _EmailPassword_Type()
)
emailPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailPassword.setStatus("current")
_RecipientTable_Object = MibTable
recipientTable = _RecipientTable_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 7, 6, 7)
)
if mibBuilder.loadTexts:
    recipientTable.setStatus("current")
_RecipientEntry_Object = MibTableRow
recipientEntry = _RecipientEntry_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 7, 6, 7, 1)
)
recipientEntry.setIndexNames(
    (0, "INOVONICS-MODEL640-MIB", "recipientIndex"),
)
if mibBuilder.loadTexts:
    recipientEntry.setStatus("current")


class _RecipientIndex_Type(Integer32):
    """Custom type recipientIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_RecipientIndex_Type.__name__ = "Integer32"
_RecipientIndex_Object = MibTableColumn
recipientIndex = _RecipientIndex_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 7, 6, 7, 1, 1),
    _RecipientIndex_Type()
)
recipientIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    recipientIndex.setStatus("current")


class _EmailAddress_Type(DisplayString):
    """Custom type emailAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_EmailAddress_Type.__name__ = "DisplayString"
_EmailAddress_Object = MibTableColumn
emailAddress = _EmailAddress_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 7, 6, 7, 1, 2),
    _EmailAddress_Type()
)
emailAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailAddress.setStatus("current")
_AudioLossEmail_Type = OnOff
_AudioLossEmail_Object = MibTableColumn
audioLossEmail = _AudioLossEmail_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 7, 6, 7, 1, 3),
    _AudioLossEmail_Type()
)
audioLossEmail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    audioLossEmail.setStatus("current")
_LowSignalEmail_Type = OnOff
_LowSignalEmail_Object = MibTableColumn
lowSignalEmail = _LowSignalEmail_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 7, 6, 7, 1, 4),
    _LowSignalEmail_Type()
)
lowSignalEmail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lowSignalEmail.setStatus("current")
_RdsLossEmail_Type = OnOff
_RdsLossEmail_Object = MibTableColumn
rdsLossEmail = _RdsLossEmail_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 7, 6, 7, 1, 5),
    _RdsLossEmail_Type()
)
rdsLossEmail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdsLossEmail.setStatus("current")
_PilotLossEmail_Type = OnOff
_PilotLossEmail_Object = MibTableColumn
pilotLossEmail = _PilotLossEmail_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 7, 6, 7, 1, 6),
    _PilotLossEmail_Type()
)
pilotLossEmail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pilotLossEmail.setStatus("current")
_DailyLogEmail_Type = OnOff
_DailyLogEmail_Object = MibTableColumn
dailyLogEmail = _DailyLogEmail_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 7, 6, 7, 1, 7),
    _DailyLogEmail_Type()
)
dailyLogEmail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dailyLogEmail.setStatus("current")
_WeeklyLogEmail_Type = OnOff
_WeeklyLogEmail_Object = MibTableColumn
weeklyLogEmail = _WeeklyLogEmail_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 7, 6, 7, 1, 8),
    _WeeklyLogEmail_Type()
)
weeklyLogEmail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    weeklyLogEmail.setStatus("current")
_MonthlyLogEmail_Type = OnOff
_MonthlyLogEmail_Object = MibTableColumn
monthlyLogEmail = _MonthlyLogEmail_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 7, 6, 7, 1, 9),
    _MonthlyLogEmail_Type()
)
monthlyLogEmail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    monthlyLogEmail.setStatus("current")
_AlarmLog_ObjectIdentity = ObjectIdentity
alarmLog = _AlarmLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42111, 640, 7, 7)
)


class _AlarmLogStatus_Type(Integer32):
    """Custom type alarmLogStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AlarmLogStatus_Type.__name__ = "Integer32"
_AlarmLogStatus_Object = MibScalar
alarmLogStatus = _AlarmLogStatus_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 7, 7, 1),
    _AlarmLogStatus_Type()
)
alarmLogStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmLogStatus.setStatus("current")


class _AlarmLogFullEmail_Type(Integer32):
    """Custom type alarmLogFullEmail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_AlarmLogFullEmail_Type.__name__ = "Integer32"
_AlarmLogFullEmail_Object = MibScalar
alarmLogFullEmail = _AlarmLogFullEmail_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 7, 7, 2),
    _AlarmLogFullEmail_Type()
)
alarmLogFullEmail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmLogFullEmail.setStatus("current")
_AlarmPolarity_ObjectIdentity = ObjectIdentity
alarmPolarity = _AlarmPolarity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42111, 640, 7, 8)
)


class _AudioLossPolarity_Type(Integer32):
    """Custom type audioLossPolarity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("activeGround", 0),
          ("activeOpen", 1))
    )


_AudioLossPolarity_Type.__name__ = "Integer32"
_AudioLossPolarity_Object = MibScalar
audioLossPolarity = _AudioLossPolarity_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 7, 8, 1),
    _AudioLossPolarity_Type()
)
audioLossPolarity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    audioLossPolarity.setStatus("current")


class _LowSignalPolarity_Type(Integer32):
    """Custom type lowSignalPolarity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("activeGround", 0),
          ("activeOpen", 1))
    )


_LowSignalPolarity_Type.__name__ = "Integer32"
_LowSignalPolarity_Object = MibScalar
lowSignalPolarity = _LowSignalPolarity_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 7, 8, 2),
    _LowSignalPolarity_Type()
)
lowSignalPolarity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lowSignalPolarity.setStatus("current")


class _RdsLossPolarity_Type(Integer32):
    """Custom type rdsLossPolarity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("activeGround", 0),
          ("activeOpen", 1))
    )


_RdsLossPolarity_Type.__name__ = "Integer32"
_RdsLossPolarity_Object = MibScalar
rdsLossPolarity = _RdsLossPolarity_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 7, 8, 3),
    _RdsLossPolarity_Type()
)
rdsLossPolarity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdsLossPolarity.setStatus("current")


class _PilotLossPolarity_Type(Integer32):
    """Custom type pilotLossPolarity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("activeGround", 0),
          ("activeOpen", 1))
    )


_PilotLossPolarity_Type.__name__ = "Integer32"
_PilotLossPolarity_Object = MibScalar
pilotLossPolarity = _PilotLossPolarity_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 7, 8, 4),
    _PilotLossPolarity_Type()
)
pilotLossPolarity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pilotLossPolarity.setStatus("current")
_Region_ObjectIdentity = ObjectIdentity
region = _Region_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42111, 640, 7, 9)
)


class _TuningSteps_Type(Integer32):
    """Custom type tuningSteps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tune10kHz", 0),
          ("tune100kHz", 1),
          ("tune200kHz", 2))
    )


_TuningSteps_Type.__name__ = "Integer32"
_TuningSteps_Object = MibScalar
tuningSteps = _TuningSteps_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 7, 9, 1),
    _TuningSteps_Type()
)
tuningSteps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tuningSteps.setStatus("current")


class _Deemphasis_Type(Integer32):
    """Custom type deemphasis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("deemph50us", 0),
          ("deemph75us", 1))
    )


_Deemphasis_Type.__name__ = "Integer32"
_Deemphasis_Object = MibScalar
deemphasis = _Deemphasis_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 7, 9, 2),
    _Deemphasis_Type()
)
deemphasis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deemphasis.setStatus("current")


class _RdsDecodeMode_Type(Integer32):
    """Custom type rdsDecodeMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("rds", 0),
          ("rbds", 1))
    )


_RdsDecodeMode_Type.__name__ = "Integer32"
_RdsDecodeMode_Object = MibScalar
rdsDecodeMode = _RdsDecodeMode_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 7, 9, 3),
    _RdsDecodeMode_Type()
)
rdsDecodeMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdsDecodeMode.setStatus("current")
_TestOscillator_ObjectIdentity = ObjectIdentity
testOscillator = _TestOscillator_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42111, 640, 7, 10)
)


class _OscMode_Type(Integer32):
    """Custom type oscMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("oscOff", 0),
          ("oscLeft", 1),
          ("oscRight", 2),
          ("oscLeftRight", 3))
    )


_OscMode_Type.__name__ = "Integer32"
_OscMode_Object = MibScalar
oscMode = _OscMode_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 7, 10, 1),
    _OscMode_Type()
)
oscMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oscMode.setStatus("current")


class _OscFrequency_Type(Integer32):
    """Custom type oscFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 20000),
    )


_OscFrequency_Type.__name__ = "Integer32"
_OscFrequency_Object = MibScalar
oscFrequency = _OscFrequency_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 7, 10, 2),
    _OscFrequency_Type()
)
oscFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oscFrequency.setStatus("current")


class _OscLevel_Type(Integer32):
    """Custom type oscLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-30, 0),
    )


_OscLevel_Type.__name__ = "Integer32"
_OscLevel_Object = MibScalar
oscLevel = _OscLevel_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 7, 10, 3),
    _OscLevel_Type()
)
oscLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oscLevel.setStatus("current")
_Passwords_ObjectIdentity = ObjectIdentity
passwords = _Passwords_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42111, 640, 8)
)


class _FrontPanelPassword_Type(DisplayString):
    """Custom type frontPanelPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_FrontPanelPassword_Type.__name__ = "DisplayString"
_FrontPanelPassword_Object = MibScalar
frontPanelPassword = _FrontPanelPassword_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 8, 1),
    _FrontPanelPassword_Type()
)
frontPanelPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frontPanelPassword.setStatus("current")


class _WebpagesPassword_Type(DisplayString):
    """Custom type webpagesPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_WebpagesPassword_Type.__name__ = "DisplayString"
_WebpagesPassword_Object = MibScalar
webpagesPassword = _WebpagesPassword_Object(
    (1, 3, 6, 1, 4, 1, 42111, 640, 8, 2),
    _WebpagesPassword_Type()
)
webpagesPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    webpagesPassword.setStatus("current")

# Managed Objects groups


# Notification objects

audioLossTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 42111, 640, 1, 0, 1)
)
audioLossTrap.setObjects(
    ("INOVONICS-MODEL640-MIB", "audioLossAlarm")
)
if mibBuilder.loadTexts:
    audioLossTrap.setStatus(
        "current"
    )

lowSignalTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 42111, 640, 1, 0, 2)
)
lowSignalTrap.setObjects(
    ("INOVONICS-MODEL640-MIB", "lowSignalAlarm")
)
if mibBuilder.loadTexts:
    lowSignalTrap.setStatus(
        "current"
    )

rdsErrorTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 42111, 640, 1, 0, 3)
)
rdsErrorTrap.setObjects(
    ("INOVONICS-MODEL640-MIB", "rdsErrorAlarm")
)
if mibBuilder.loadTexts:
    rdsErrorTrap.setStatus(
        "current"
    )

pilotLossTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 42111, 640, 1, 0, 4)
)
pilotLossTrap.setObjects(
    ("INOVONICS-MODEL640-MIB", "pilotLossAlarm")
)
if mibBuilder.loadTexts:
    pilotLossTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INOVONICS-MODEL640-MIB",
    **{"OnOff": OnOff,
       "inovonicsBroadcast": inovonicsBroadcast,
       "model640": model640,
       "traps": traps,
       "notifications": notifications,
       "audioLossTrap": audioLossTrap,
       "lowSignalTrap": lowSignalTrap,
       "rdsErrorTrap": rdsErrorTrap,
       "pilotLossTrap": pilotLossTrap,
       "product": product,
       "serial": serial,
       "version": version,
       "date": date,
       "nowPlaying": nowPlaying,
       "frequency": frequency,
       "currentPreset": currentPreset,
       "rssi": rssi,
       "bandwidth": bandwidth,
       "multipath": multipath,
       "noise": noise,
       "leftLeveldB": leftLeveldB,
       "rightLeveldB": rightLeveldB,
       "leftPlusRightLeveldB": leftPlusRightLeveldB,
       "leftMinusRightLeveldB": leftMinusRightLeveldB,
       "receptionTools": receptionTools,
       "bandwidthIF": bandwidthIF,
       "bandwidthMode": bandwidthMode,
       "fixedBandwidth": fixedBandwidth,
       "stereoBlend": stereoBlend,
       "stereoBlendAmount": stereoBlendAmount,
       "stereoBlendAuto": stereoBlendAuto,
       "stereoBlendUseRSSI": stereoBlendUseRSSI,
       "stereoBlendThresholdRSSI": stereoBlendThresholdRSSI,
       "stereoBlendUseUSN": stereoBlendUseUSN,
       "stereoBlendThresholdUSN": stereoBlendThresholdUSN,
       "stereoBlendUseMultipath": stereoBlendUseMultipath,
       "stereoBlendThresholdMultipath": stereoBlendThresholdMultipath,
       "highBlend": highBlend,
       "highBlendAmount": highBlendAmount,
       "highBlendAuto": highBlendAuto,
       "highBlendUseRSSI": highBlendUseRSSI,
       "highBlendThresholdRSSI": highBlendThresholdRSSI,
       "highBlendUseUSN": highBlendUseUSN,
       "highBlendThresholdUSN": highBlendThresholdUSN,
       "highBlendUseMultipath": highBlendUseMultipath,
       "highBlendThresholdMultipath": highBlendThresholdMultipath,
       "bandBlend": bandBlend,
       "bandBlendEnable": bandBlendEnable,
       "bandBlendControl": bandBlendControl,
       "bandBlendLF": bandBlendLF,
       "bandBlend2k": bandBlend2k,
       "bandBlend5k": bandBlend5k,
       "bandBlendHF": bandBlendHF,
       "highcut": highcut,
       "highcutAmount": highcutAmount,
       "highcutAuto": highcutAuto,
       "highcutUseRSSI": highcutUseRSSI,
       "highcutThresholdRSSI": highcutThresholdRSSI,
       "highcutUseUSN": highcutUseUSN,
       "highcutThresholdUSN": highcutThresholdUSN,
       "highcutUseMultipath": highcutUseMultipath,
       "highcutThresholdMultipath": highcutThresholdMultipath,
       "monoStereo": monoStereo,
       "multipathSuppression": multipathSuppression,
       "channelEqualizer": channelEqualizer,
       "rds": rds,
       "pi": pi,
       "call": call,
       "ps": ps,
       "rt": rt,
       "pty": pty,
       "ptyn": ptyn,
       "rdsTime": rdsTime,
       "ms": ms,
       "di": di,
       "tp": tp,
       "ta": ta,
       "alarms": alarms,
       "alarmStatus": alarmStatus,
       "audioLossAlarm": audioLossAlarm,
       "lowSignalAlarm": lowSignalAlarm,
       "rdsErrorAlarm": rdsErrorAlarm,
       "pilotLossAlarm": pilotLossAlarm,
       "audioLoss": audioLoss,
       "audioLossEnable": audioLossEnable,
       "audioLossThreshOn": audioLossThreshOn,
       "audioLossThreshOff": audioLossThreshOff,
       "audioLossTimeOn": audioLossTimeOn,
       "audioLossTimeOff": audioLossTimeOff,
       "lowSignal": lowSignal,
       "lowSignalEnable": lowSignalEnable,
       "lowSignalMute": lowSignalMute,
       "lowSignalThreshOn": lowSignalThreshOn,
       "lowSignalThreshOff": lowSignalThreshOff,
       "lowSignalTimeOn": lowSignalTimeOn,
       "lowSignalTimeOff": lowSignalTimeOff,
       "rdsLoss": rdsLoss,
       "rdsLossEnable": rdsLossEnable,
       "rdsPIErrorEnable": rdsPIErrorEnable,
       "rdsPICode": rdsPICode,
       "rdsLossTimeOn": rdsLossTimeOn,
       "rdsLossTimeOff": rdsLossTimeOff,
       "pilotLoss": pilotLoss,
       "pilotLossEnable": pilotLossEnable,
       "pilotLossTimeOn": pilotLossTimeOn,
       "pilotLossTimeOff": pilotLossTimeOff,
       "setup": setup,
       "outputs": outputs,
       "analogLevel": analogLevel,
       "analogDeemphasis": analogDeemphasis,
       "digitalLevel": digitalLevel,
       "digitalDeemphasis": digitalDeemphasis,
       "mpxLevel": mpxLevel,
       "mpxClipping": mpxClipping,
       "network": network,
       "dhcp": dhcp,
       "ip": ip,
       "gateway": gateway,
       "subnet": subnet,
       "dns": dns,
       "httpPort": httpPort,
       "hostname": hostname,
       "mac": mac,
       "dynDNS": dynDNS,
       "ddnsMode": ddnsMode,
       "ddnsHostname": ddnsHostname,
       "ddnsUsername": ddnsUsername,
       "ddnsPassword": ddnsPassword,
       "ddnsStatus": ddnsStatus,
       "time": time,
       "timezone": timezone,
       "dst": dst,
       "autodst": autodst,
       "timeServer": timeServer,
       "snmp": snmp,
       "snmpMode": snmpMode,
       "snmpReadCommunity": snmpReadCommunity,
       "snmpWriteCommunity": snmpWriteCommunity,
       "snmpPort": snmpPort,
       "snmpTrapsPort": snmpTrapsPort,
       "snmpTrapDestination1": snmpTrapDestination1,
       "snmpTrapDestination2": snmpTrapDestination2,
       "snmpTrapDestination3": snmpTrapDestination3,
       "email": email,
       "smtpServer": smtpServer,
       "smtpPort": smtpPort,
       "ssl": ssl,
       "emailFrom": emailFrom,
       "emailUsername": emailUsername,
       "emailPassword": emailPassword,
       "recipientTable": recipientTable,
       "recipientEntry": recipientEntry,
       "recipientIndex": recipientIndex,
       "emailAddress": emailAddress,
       "audioLossEmail": audioLossEmail,
       "lowSignalEmail": lowSignalEmail,
       "rdsLossEmail": rdsLossEmail,
       "pilotLossEmail": pilotLossEmail,
       "dailyLogEmail": dailyLogEmail,
       "weeklyLogEmail": weeklyLogEmail,
       "monthlyLogEmail": monthlyLogEmail,
       "alarmLog": alarmLog,
       "alarmLogStatus": alarmLogStatus,
       "alarmLogFullEmail": alarmLogFullEmail,
       "alarmPolarity": alarmPolarity,
       "audioLossPolarity": audioLossPolarity,
       "lowSignalPolarity": lowSignalPolarity,
       "rdsLossPolarity": rdsLossPolarity,
       "pilotLossPolarity": pilotLossPolarity,
       "region": region,
       "tuningSteps": tuningSteps,
       "deemphasis": deemphasis,
       "rdsDecodeMode": rdsDecodeMode,
       "testOscillator": testOscillator,
       "oscMode": oscMode,
       "oscFrequency": oscFrequency,
       "oscLevel": oscLevel,
       "passwords": passwords,
       "frontPanelPassword": frontPanelPassword,
       "webpagesPassword": webpagesPassword}
)
