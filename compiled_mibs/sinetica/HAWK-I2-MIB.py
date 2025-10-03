# SNMP MIB module (HAWK-I2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\sinetica\HAWK-I2-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:28:13 2025
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hawki2MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3711, 24)
)
if mibBuilder.loadTexts:
    hawki2MIB.setRevisions(
        ("2006-06-27 12:00",
         "2006-03-07 12:00")
    )


# Types definitions



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



class ContactState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("open", 1),
          ("closed", 2))
    )



class InputContactState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("open", 1),
          ("closed", 2),
          ("armed", 3),
          ("triggered", 4))
    )



class RelayState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )



class OutputControlState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("activate", 1),
          ("deactivate", 2),
          ("logic", 3))
    )



class EnableState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )



class InputDataType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              255)
        )
    )
    namedValues = NamedValues(
        *(("autodetect", 1),
          ("temperature", 2),
          ("humidity", 3),
          ("analogue", 4),
          ("contact", 5),
          ("inactive", 255))
    )



# MIB Managed Objects in the order of their OIDs

_Sinetica_ObjectIdentity = ObjectIdentity
sinetica = _Sinetica_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3711)
)
_Traps_ObjectIdentity = ObjectIdentity
traps = _Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3711, 24, 0)
)
_V1_ObjectIdentity = ObjectIdentity
v1 = _V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1)
)
_Objects_ObjectIdentity = ObjectIdentity
objects = _Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1)
)
_Inputs_ObjectIdentity = ObjectIdentity
inputs = _Inputs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 1)
)
_IpCommon_ObjectIdentity = ObjectIdentity
ipCommon = _IpCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 1, 1)
)
_IpEnable_ObjectIdentity = ObjectIdentity
ipEnable = _IpEnable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 1, 1, 1)
)


class _IpSelect_Type(Integer32):
    """Custom type ipSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_IpSelect_Type.__name__ = "Integer32"
_IpSelect_Object = MibScalar
ipSelect = _IpSelect_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 1, 1, 1, 1),
    _IpSelect_Type()
)
ipSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSelect.setStatus("current")
_IpInsert_Type = InputDataType
_IpInsert_Object = MibScalar
ipInsert = _IpInsert_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 1, 1, 1, 2),
    _IpInsert_Type()
)
ipInsert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipInsert.setStatus("current")
_IpTHA_ObjectIdentity = ObjectIdentity
ipTHA = _IpTHA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 1, 2)
)


class _IpTempScaleFlag_Type(Integer32):
    """Custom type ipTempScaleFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("celsius", 1),
          ("fahrenheit", 2),
          ("kelvin", 3))
    )


_IpTempScaleFlag_Type.__name__ = "Integer32"
_IpTempScaleFlag_Object = MibScalar
ipTempScaleFlag = _IpTempScaleFlag_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 1, 2, 1),
    _IpTempScaleFlag_Type()
)
ipTempScaleFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipTempScaleFlag.setStatus("current")
_IpTHATable_Object = MibTable
ipTHATable = _IpTHATable_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    ipTHATable.setStatus("current")
_IpTHAEntry_Object = MibTableRow
ipTHAEntry = _IpTHAEntry_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 1, 2, 2, 1)
)
ipTHAEntry.setIndexNames(
    (0, "HAWK-I2-MIB", "ipTHAChan"),
)
if mibBuilder.loadTexts:
    ipTHAEntry.setStatus("current")


class _IpTHAChan_Type(Integer32):
    """Custom type ipTHAChan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_IpTHAChan_Type.__name__ = "Integer32"
_IpTHAChan_Object = MibTableColumn
ipTHAChan = _IpTHAChan_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 1, 2, 2, 1, 1),
    _IpTHAChan_Type()
)
ipTHAChan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipTHAChan.setStatus("current")
_IpTHARS_Type = RowStatus
_IpTHARS_Object = MibTableColumn
ipTHARS = _IpTHARS_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 1, 2, 2, 1, 2),
    _IpTHARS_Type()
)
ipTHARS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipTHARS.setStatus("current")


class _IpTHAName_Type(DisplayString):
    """Custom type ipTHAName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_IpTHAName_Type.__name__ = "DisplayString"
_IpTHAName_Object = MibTableColumn
ipTHAName = _IpTHAName_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 1, 2, 2, 1, 3),
    _IpTHAName_Type()
)
ipTHAName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipTHAName.setStatus("current")


class _IpTHALocn_Type(DisplayString):
    """Custom type ipTHALocn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_IpTHALocn_Type.__name__ = "DisplayString"
_IpTHALocn_Object = MibTableColumn
ipTHALocn = _IpTHALocn_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 1, 2, 2, 1, 4),
    _IpTHALocn_Type()
)
ipTHALocn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipTHALocn.setStatus("current")
_IpTHAAutoDetect_Type = TruthValue
_IpTHAAutoDetect_Object = MibTableColumn
ipTHAAutoDetect = _IpTHAAutoDetect_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 1, 2, 2, 1, 5),
    _IpTHAAutoDetect_Type()
)
ipTHAAutoDetect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipTHAAutoDetect.setStatus("current")
_IpTHAType_Type = InputDataType
_IpTHAType_Object = MibTableColumn
ipTHAType = _IpTHAType_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 1, 2, 2, 1, 6),
    _IpTHAType_Type()
)
ipTHAType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipTHAType.setStatus("current")


class _IpTHAValue_Type(Integer32):
    """Custom type ipTHAValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-200, 1000),
    )


_IpTHAValue_Type.__name__ = "Integer32"
_IpTHAValue_Object = MibTableColumn
ipTHAValue = _IpTHAValue_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 1, 2, 2, 1, 7),
    _IpTHAValue_Type()
)
ipTHAValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipTHAValue.setStatus("current")


class _IpTHAScaling_Type(Integer32):
    """Custom type ipTHAScaling based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_IpTHAScaling_Type.__name__ = "Integer32"
_IpTHAScaling_Object = MibTableColumn
ipTHAScaling = _IpTHAScaling_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 1, 2, 2, 1, 8),
    _IpTHAScaling_Type()
)
ipTHAScaling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipTHAScaling.setStatus("current")


class _IpTHAOffset_Type(Integer32):
    """Custom type ipTHAOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_IpTHAOffset_Type.__name__ = "Integer32"
_IpTHAOffset_Object = MibTableColumn
ipTHAOffset = _IpTHAOffset_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 1, 2, 2, 1, 9),
    _IpTHAOffset_Type()
)
ipTHAOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipTHAOffset.setStatus("current")


class _IpTHAHysteresis_Type(Integer32):
    """Custom type ipTHAHysteresis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_IpTHAHysteresis_Type.__name__ = "Integer32"
_IpTHAHysteresis_Object = MibTableColumn
ipTHAHysteresis = _IpTHAHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 1, 2, 2, 1, 10),
    _IpTHAHysteresis_Type()
)
ipTHAHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipTHAHysteresis.setStatus("current")
_IpTHATrapsCfg_ObjectIdentity = ObjectIdentity
ipTHATrapsCfg = _IpTHATrapsCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 1, 2, 3)
)
_IpTHAThreshTable_Object = MibTable
ipTHAThreshTable = _IpTHAThreshTable_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    ipTHAThreshTable.setStatus("current")
_IpTHAThreshEntry_Object = MibTableRow
ipTHAThreshEntry = _IpTHAThreshEntry_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 1, 2, 3, 1, 1)
)
ipTHAThreshEntry.setIndexNames(
    (0, "HAWK-I2-MIB", "ipTHAThreshChan"),
)
if mibBuilder.loadTexts:
    ipTHAThreshEntry.setStatus("current")


class _IpTHAThreshChan_Type(Integer32):
    """Custom type ipTHAThreshChan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_IpTHAThreshChan_Type.__name__ = "Integer32"
_IpTHAThreshChan_Object = MibTableColumn
ipTHAThreshChan = _IpTHAThreshChan_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 1, 2, 3, 1, 1, 1),
    _IpTHAThreshChan_Type()
)
ipTHAThreshChan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipTHAThreshChan.setStatus("current")
_IpTHAThreshRS_Type = RowStatus
_IpTHAThreshRS_Object = MibTableColumn
ipTHAThreshRS = _IpTHAThreshRS_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 1, 2, 3, 1, 1, 2),
    _IpTHAThreshRS_Type()
)
ipTHAThreshRS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipTHAThreshRS.setStatus("current")


class _IpTHAUCL_Type(Integer32):
    """Custom type ipTHAUCL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-200, 1000),
    )


_IpTHAUCL_Type.__name__ = "Integer32"
_IpTHAUCL_Object = MibTableColumn
ipTHAUCL = _IpTHAUCL_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 1, 2, 3, 1, 1, 3),
    _IpTHAUCL_Type()
)
ipTHAUCL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipTHAUCL.setStatus("current")


class _IpTHAUWL_Type(Integer32):
    """Custom type ipTHAUWL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-200, 1000),
    )


_IpTHAUWL_Type.__name__ = "Integer32"
_IpTHAUWL_Object = MibTableColumn
ipTHAUWL = _IpTHAUWL_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 1, 2, 3, 1, 1, 4),
    _IpTHAUWL_Type()
)
ipTHAUWL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipTHAUWL.setStatus("current")


class _IpTHALWL_Type(Integer32):
    """Custom type ipTHALWL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-200, 1000),
    )


_IpTHALWL_Type.__name__ = "Integer32"
_IpTHALWL_Object = MibTableColumn
ipTHALWL = _IpTHALWL_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 1, 2, 3, 1, 1, 5),
    _IpTHALWL_Type()
)
ipTHALWL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipTHALWL.setStatus("current")


class _IpTHALCL_Type(Integer32):
    """Custom type ipTHALCL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-200, 1000),
    )


_IpTHALCL_Type.__name__ = "Integer32"
_IpTHALCL_Object = MibTableColumn
ipTHALCL = _IpTHALCL_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 1, 2, 3, 1, 1, 6),
    _IpTHALCL_Type()
)
ipTHALCL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipTHALCL.setStatus("current")
_IpTHATrapEnTable_Object = MibTable
ipTHATrapEnTable = _IpTHATrapEnTable_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 1, 2, 3, 2)
)
if mibBuilder.loadTexts:
    ipTHATrapEnTable.setStatus("current")
_IpTHATrapEnEntry_Object = MibTableRow
ipTHATrapEnEntry = _IpTHATrapEnEntry_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 1, 2, 3, 2, 1)
)
ipTHATrapEnEntry.setIndexNames(
    (0, "HAWK-I2-MIB", "ipTHATrapEnChan"),
)
if mibBuilder.loadTexts:
    ipTHATrapEnEntry.setStatus("current")


class _IpTHATrapEnChan_Type(Integer32):
    """Custom type ipTHATrapEnChan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_IpTHATrapEnChan_Type.__name__ = "Integer32"
_IpTHATrapEnChan_Object = MibTableColumn
ipTHATrapEnChan = _IpTHATrapEnChan_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 1, 2, 3, 2, 1, 1),
    _IpTHATrapEnChan_Type()
)
ipTHATrapEnChan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipTHATrapEnChan.setStatus("current")
_IpTHATrapEnRS_Type = RowStatus
_IpTHATrapEnRS_Object = MibTableColumn
ipTHATrapEnRS = _IpTHATrapEnRS_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 1, 2, 3, 2, 1, 2),
    _IpTHATrapEnRS_Type()
)
ipTHATrapEnRS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipTHATrapEnRS.setStatus("current")
_IpTHAUCLTrapEn_Type = TruthValue
_IpTHAUCLTrapEn_Object = MibTableColumn
ipTHAUCLTrapEn = _IpTHAUCLTrapEn_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 1, 2, 3, 2, 1, 3),
    _IpTHAUCLTrapEn_Type()
)
ipTHAUCLTrapEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipTHAUCLTrapEn.setStatus("current")
_IpTHAUWLTrapEn_Type = TruthValue
_IpTHAUWLTrapEn_Object = MibTableColumn
ipTHAUWLTrapEn = _IpTHAUWLTrapEn_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 1, 2, 3, 2, 1, 4),
    _IpTHAUWLTrapEn_Type()
)
ipTHAUWLTrapEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipTHAUWLTrapEn.setStatus("current")
_IpTHALWLTrapEn_Type = TruthValue
_IpTHALWLTrapEn_Object = MibTableColumn
ipTHALWLTrapEn = _IpTHALWLTrapEn_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 1, 2, 3, 2, 1, 5),
    _IpTHALWLTrapEn_Type()
)
ipTHALWLTrapEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipTHALWLTrapEn.setStatus("current")
_IpTHALCLTrapEn_Type = TruthValue
_IpTHALCLTrapEn_Object = MibTableColumn
ipTHALCLTrapEn = _IpTHALCLTrapEn_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 1, 2, 3, 2, 1, 6),
    _IpTHALCLTrapEn_Type()
)
ipTHALCLTrapEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipTHALCLTrapEn.setStatus("current")
_IpTHATrapPerTable_Object = MibTable
ipTHATrapPerTable = _IpTHATrapPerTable_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 1, 2, 3, 3)
)
if mibBuilder.loadTexts:
    ipTHATrapPerTable.setStatus("current")
_IpTHATrapPerEntry_Object = MibTableRow
ipTHATrapPerEntry = _IpTHATrapPerEntry_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 1, 2, 3, 3, 1)
)
ipTHATrapPerEntry.setIndexNames(
    (0, "HAWK-I2-MIB", "ipTHATrapPerChan"),
)
if mibBuilder.loadTexts:
    ipTHATrapPerEntry.setStatus("current")


class _IpTHATrapPerChan_Type(Integer32):
    """Custom type ipTHATrapPerChan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_IpTHATrapPerChan_Type.__name__ = "Integer32"
_IpTHATrapPerChan_Object = MibTableColumn
ipTHATrapPerChan = _IpTHATrapPerChan_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 1, 2, 3, 3, 1, 1),
    _IpTHATrapPerChan_Type()
)
ipTHATrapPerChan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipTHATrapPerChan.setStatus("current")
_IpTHATrapPerRS_Type = RowStatus
_IpTHATrapPerRS_Object = MibTableColumn
ipTHATrapPerRS = _IpTHATrapPerRS_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 1, 2, 3, 3, 1, 2),
    _IpTHATrapPerRS_Type()
)
ipTHATrapPerRS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipTHATrapPerRS.setStatus("current")


class _IpTHATrapUCLPer_Type(Integer32):
    """Custom type ipTHATrapUCLPer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 32000),
    )


_IpTHATrapUCLPer_Type.__name__ = "Integer32"
_IpTHATrapUCLPer_Object = MibTableColumn
ipTHATrapUCLPer = _IpTHATrapUCLPer_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 1, 2, 3, 3, 1, 3),
    _IpTHATrapUCLPer_Type()
)
ipTHATrapUCLPer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipTHATrapUCLPer.setStatus("current")


class _IpTHATrapUWLPer_Type(Integer32):
    """Custom type ipTHATrapUWLPer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 32000),
    )


_IpTHATrapUWLPer_Type.__name__ = "Integer32"
_IpTHATrapUWLPer_Object = MibTableColumn
ipTHATrapUWLPer = _IpTHATrapUWLPer_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 1, 2, 3, 3, 1, 4),
    _IpTHATrapUWLPer_Type()
)
ipTHATrapUWLPer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipTHATrapUWLPer.setStatus("current")


class _IpTHATrapLWLPer_Type(Integer32):
    """Custom type ipTHATrapLWLPer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 32000),
    )


_IpTHATrapLWLPer_Type.__name__ = "Integer32"
_IpTHATrapLWLPer_Object = MibTableColumn
ipTHATrapLWLPer = _IpTHATrapLWLPer_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 1, 2, 3, 3, 1, 5),
    _IpTHATrapLWLPer_Type()
)
ipTHATrapLWLPer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipTHATrapLWLPer.setStatus("current")


class _IpTHATrapLCLPer_Type(Integer32):
    """Custom type ipTHATrapLCLPer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 32000),
    )


_IpTHATrapLCLPer_Type.__name__ = "Integer32"
_IpTHATrapLCLPer_Object = MibTableColumn
ipTHATrapLCLPer = _IpTHATrapLCLPer_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 1, 2, 3, 3, 1, 6),
    _IpTHATrapLCLPer_Type()
)
ipTHATrapLCLPer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipTHATrapLCLPer.setStatus("current")
_IpContact_ObjectIdentity = ObjectIdentity
ipContact = _IpContact_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 1, 3)
)
_IpContTable_Object = MibTable
ipContTable = _IpContTable_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    ipContTable.setStatus("current")
_IpContEntry_Object = MibTableRow
ipContEntry = _IpContEntry_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 1, 3, 1, 1)
)
ipContEntry.setIndexNames(
    (0, "HAWK-I2-MIB", "ipContChan"),
)
if mibBuilder.loadTexts:
    ipContEntry.setStatus("current")


class _IpContChan_Type(Integer32):
    """Custom type ipContChan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_IpContChan_Type.__name__ = "Integer32"
_IpContChan_Object = MibTableColumn
ipContChan = _IpContChan_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 1, 3, 1, 1, 1),
    _IpContChan_Type()
)
ipContChan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipContChan.setStatus("current")
_IpContRS_Type = RowStatus
_IpContRS_Object = MibTableColumn
ipContRS = _IpContRS_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 1, 3, 1, 1, 2),
    _IpContRS_Type()
)
ipContRS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipContRS.setStatus("current")


class _IpContName_Type(DisplayString):
    """Custom type ipContName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_IpContName_Type.__name__ = "DisplayString"
_IpContName_Object = MibTableColumn
ipContName = _IpContName_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 1, 3, 1, 1, 3),
    _IpContName_Type()
)
ipContName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipContName.setStatus("current")


class _IpContLocn_Type(DisplayString):
    """Custom type ipContLocn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_IpContLocn_Type.__name__ = "DisplayString"
_IpContLocn_Object = MibTableColumn
ipContLocn = _IpContLocn_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 1, 3, 1, 1, 4),
    _IpContLocn_Type()
)
ipContLocn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipContLocn.setStatus("current")
_IpContAutoDetect_Type = TruthValue
_IpContAutoDetect_Object = MibTableColumn
ipContAutoDetect = _IpContAutoDetect_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 1, 3, 1, 1, 5),
    _IpContAutoDetect_Type()
)
ipContAutoDetect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipContAutoDetect.setStatus("current")
_IpContNormState_Type = ContactState
_IpContNormState_Object = MibTableColumn
ipContNormState = _IpContNormState_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 1, 3, 1, 1, 6),
    _IpContNormState_Type()
)
ipContNormState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipContNormState.setStatus("current")
_IpContCurrState_Type = InputContactState
_IpContCurrState_Object = MibTableColumn
ipContCurrState = _IpContCurrState_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 1, 3, 1, 1, 7),
    _IpContCurrState_Type()
)
ipContCurrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipContCurrState.setStatus("current")


class _IpContTrigMode_Type(Integer32):
    """Custom type ipContTrigMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("positiveEdge", 1),
          ("negativeEdge", 2),
          ("level", 3))
    )


_IpContTrigMode_Type.__name__ = "Integer32"
_IpContTrigMode_Object = MibTableColumn
ipContTrigMode = _IpContTrigMode_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 1, 3, 1, 1, 8),
    _IpContTrigMode_Type()
)
ipContTrigMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipContTrigMode.setStatus("current")
_IpContReset_Type = Unsigned32
_IpContReset_Object = MibTableColumn
ipContReset = _IpContReset_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 1, 3, 1, 1, 9),
    _IpContReset_Type()
)
ipContReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipContReset.setStatus("current")


class _IpContTrapEn_Type(Integer32):
    """Custom type ipContTrapEn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("critical", 1),
          ("warning", 2),
          ("information", 3),
          ("disabled", 255))
    )


_IpContTrapEn_Type.__name__ = "Integer32"
_IpContTrapEn_Object = MibTableColumn
ipContTrapEn = _IpContTrapEn_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 1, 3, 1, 1, 10),
    _IpContTrapEn_Type()
)
ipContTrapEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipContTrapEn.setStatus("current")


class _IpContTrapPeriod_Type(Integer32):
    """Custom type ipContTrapPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 32000),
    )


_IpContTrapPeriod_Type.__name__ = "Integer32"
_IpContTrapPeriod_Object = MibTableColumn
ipContTrapPeriod = _IpContTrapPeriod_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 1, 3, 1, 1, 11),
    _IpContTrapPeriod_Type()
)
ipContTrapPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipContTrapPeriod.setStatus("current")
_Outputs_ObjectIdentity = ObjectIdentity
outputs = _Outputs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 2)
)
_OpEnable_ObjectIdentity = ObjectIdentity
opEnable = _OpEnable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 2, 1)
)


class _OpSelect_Type(Integer32):
    """Custom type opSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_OpSelect_Type.__name__ = "Integer32"
_OpSelect_Object = MibScalar
opSelect = _OpSelect_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 2, 1, 1),
    _OpSelect_Type()
)
opSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    opSelect.setStatus("current")
_OpInsert_Type = EnableState
_OpInsert_Object = MibScalar
opInsert = _OpInsert_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 2, 1, 2),
    _OpInsert_Type()
)
opInsert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    opInsert.setStatus("current")
_OpTable_Object = MibTable
opTable = _OpTable_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    opTable.setStatus("current")
_OpEntry_Object = MibTableRow
opEntry = _OpEntry_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 2, 2, 1)
)
opEntry.setIndexNames(
    (0, "HAWK-I2-MIB", "opChan"),
)
if mibBuilder.loadTexts:
    opEntry.setStatus("current")


class _OpChan_Type(Integer32):
    """Custom type opChan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 18),
    )


_OpChan_Type.__name__ = "Integer32"
_OpChan_Object = MibTableColumn
opChan = _OpChan_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 2, 2, 1, 1),
    _OpChan_Type()
)
opChan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opChan.setStatus("current")
_OpRS_Type = RowStatus
_OpRS_Object = MibTableColumn
opRS = _OpRS_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 2, 2, 1, 2),
    _OpRS_Type()
)
opRS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opRS.setStatus("current")


class _OpName_Type(DisplayString):
    """Custom type opName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_OpName_Type.__name__ = "DisplayString"
_OpName_Object = MibTableColumn
opName = _OpName_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 2, 2, 1, 3),
    _OpName_Type()
)
opName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    opName.setStatus("current")


class _OpLocn_Type(DisplayString):
    """Custom type opLocn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_OpLocn_Type.__name__ = "DisplayString"
_OpLocn_Object = MibTableColumn
opLocn = _OpLocn_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 2, 2, 1, 4),
    _OpLocn_Type()
)
opLocn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opLocn.setStatus("current")
_OpNormState_Type = RelayState
_OpNormState_Object = MibTableColumn
opNormState = _OpNormState_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 2, 2, 1, 5),
    _OpNormState_Type()
)
opNormState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    opNormState.setStatus("current")
_OpCurrState_Type = RelayState
_OpCurrState_Object = MibTableColumn
opCurrState = _OpCurrState_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 2, 2, 1, 6),
    _OpCurrState_Type()
)
opCurrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opCurrState.setStatus("current")
_OpOnDelTime_Type = Unsigned32
_OpOnDelTime_Object = MibTableColumn
opOnDelTime = _OpOnDelTime_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 2, 2, 1, 7),
    _OpOnDelTime_Type()
)
opOnDelTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    opOnDelTime.setStatus("current")
_OpOffDelTime_Type = Unsigned32
_OpOffDelTime_Object = MibTableColumn
opOffDelTime = _OpOffDelTime_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 2, 2, 1, 8),
    _OpOffDelTime_Type()
)
opOffDelTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    opOffDelTime.setStatus("current")
_OpBooleanEqn_Type = DisplayString
_OpBooleanEqn_Object = MibTableColumn
opBooleanEqn = _OpBooleanEqn_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 2, 2, 1, 9),
    _OpBooleanEqn_Type()
)
opBooleanEqn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    opBooleanEqn.setStatus("current")


class _OpTrapEn_Type(Integer32):
    """Custom type opTrapEn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("critical", 1),
          ("warning", 2),
          ("information", 3),
          ("disabled", 255))
    )


_OpTrapEn_Type.__name__ = "Integer32"
_OpTrapEn_Object = MibTableColumn
opTrapEn = _OpTrapEn_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 2, 2, 1, 10),
    _OpTrapEn_Type()
)
opTrapEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    opTrapEn.setStatus("current")


class _OpTrapPeriod_Type(Integer32):
    """Custom type opTrapPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 32000),
    )


_OpTrapPeriod_Type.__name__ = "Integer32"
_OpTrapPeriod_Object = MibTableColumn
opTrapPeriod = _OpTrapPeriod_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 2, 2, 1, 11),
    _OpTrapPeriod_Type()
)
opTrapPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    opTrapPeriod.setStatus("current")
_OpControlState_Type = OutputControlState
_OpControlState_Object = MibTableColumn
opControlState = _OpControlState_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 2, 2, 1, 12),
    _OpControlState_Type()
)
opControlState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    opControlState.setStatus("current")
_Keypads_ObjectIdentity = ObjectIdentity
keypads = _Keypads_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 4)
)
_KpEnable_ObjectIdentity = ObjectIdentity
kpEnable = _KpEnable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 4, 1)
)


class _KpSelect_Type(Integer32):
    """Custom type kpSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_KpSelect_Type.__name__ = "Integer32"
_KpSelect_Object = MibScalar
kpSelect = _KpSelect_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 4, 1, 1),
    _KpSelect_Type()
)
kpSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kpSelect.setStatus("current")
_KpInsert_Type = EnableState
_KpInsert_Object = MibScalar
kpInsert = _KpInsert_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 4, 1, 2),
    _KpInsert_Type()
)
kpInsert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kpInsert.setStatus("current")
_KpCtlTable_Object = MibTable
kpCtlTable = _KpCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 4, 2)
)
if mibBuilder.loadTexts:
    kpCtlTable.setStatus("current")
_KpCtlEntry_Object = MibTableRow
kpCtlEntry = _KpCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 4, 2, 1)
)
kpCtlEntry.setIndexNames(
    (0, "HAWK-I2-MIB", "kpNumber"),
)
if mibBuilder.loadTexts:
    kpCtlEntry.setStatus("current")


class _KpNumber_Type(Integer32):
    """Custom type kpNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_KpNumber_Type.__name__ = "Integer32"
_KpNumber_Object = MibTableColumn
kpNumber = _KpNumber_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 4, 2, 1, 1),
    _KpNumber_Type()
)
kpNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpNumber.setStatus("current")
_KpRS_Type = RowStatus
_KpRS_Object = MibTableColumn
kpRS = _KpRS_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 4, 2, 1, 2),
    _KpRS_Type()
)
kpRS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpRS.setStatus("current")


class _KpManufacturer_Type(DisplayString):
    """Custom type kpManufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_KpManufacturer_Type.__name__ = "DisplayString"
_KpManufacturer_Object = MibTableColumn
kpManufacturer = _KpManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 4, 2, 1, 3),
    _KpManufacturer_Type()
)
kpManufacturer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kpManufacturer.setStatus("current")


class _KpName_Type(DisplayString):
    """Custom type kpName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_KpName_Type.__name__ = "DisplayString"
_KpName_Object = MibTableColumn
kpName = _KpName_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 4, 2, 1, 4),
    _KpName_Type()
)
kpName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kpName.setStatus("current")
_KpDoorLatchTimeOut_Type = Unsigned32
_KpDoorLatchTimeOut_Object = MibTableColumn
kpDoorLatchTimeOut = _KpDoorLatchTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 4, 2, 1, 5),
    _KpDoorLatchTimeOut_Type()
)
kpDoorLatchTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kpDoorLatchTimeOut.setStatus("current")


class _KpRtnToStndbyTimeOut_Type(Integer32):
    """Custom type kpRtnToStndbyTimeOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_KpRtnToStndbyTimeOut_Type.__name__ = "Integer32"
_KpRtnToStndbyTimeOut_Object = MibTableColumn
kpRtnToStndbyTimeOut = _KpRtnToStndbyTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 4, 2, 1, 6),
    _KpRtnToStndbyTimeOut_Type()
)
kpRtnToStndbyTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kpRtnToStndbyTimeOut.setStatus("current")
_KpEntryCodeValid_Type = TruthValue
_KpEntryCodeValid_Object = MibTableColumn
kpEntryCodeValid = _KpEntryCodeValid_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 4, 2, 1, 7),
    _KpEntryCodeValid_Type()
)
kpEntryCodeValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpEntryCodeValid.setStatus("current")


class _KpDoorOpenTimeOut_Type(Integer32):
    """Custom type kpDoorOpenTimeOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_KpDoorOpenTimeOut_Type.__name__ = "Integer32"
_KpDoorOpenTimeOut_Object = MibTableColumn
kpDoorOpenTimeOut = _KpDoorOpenTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 4, 2, 1, 8),
    _KpDoorOpenTimeOut_Type()
)
kpDoorOpenTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kpDoorOpenTimeOut.setStatus("current")
_KpRemoteDoorOpen_Type = TruthValue
_KpRemoteDoorOpen_Object = MibTableColumn
kpRemoteDoorOpen = _KpRemoteDoorOpen_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 4, 2, 1, 9),
    _KpRemoteDoorOpen_Type()
)
kpRemoteDoorOpen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kpRemoteDoorOpen.setStatus("current")


class _KpInUseTrapEn_Type(Integer32):
    """Custom type kpInUseTrapEn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("critical", 1),
          ("warning", 2),
          ("information", 3),
          ("disabled", 255))
    )


_KpInUseTrapEn_Type.__name__ = "Integer32"
_KpInUseTrapEn_Object = MibTableColumn
kpInUseTrapEn = _KpInUseTrapEn_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 4, 2, 1, 10),
    _KpInUseTrapEn_Type()
)
kpInUseTrapEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kpInUseTrapEn.setStatus("current")
_Acus_ObjectIdentity = ObjectIdentity
acus = _Acus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 5)
)
_AcuEnable_ObjectIdentity = ObjectIdentity
acuEnable = _AcuEnable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 5, 1)
)


class _AcuSelect_Type(Integer32):
    """Custom type acuSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_AcuSelect_Type.__name__ = "Integer32"
_AcuSelect_Object = MibScalar
acuSelect = _AcuSelect_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 5, 1, 1),
    _AcuSelect_Type()
)
acuSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acuSelect.setStatus("current")
_AcuInsert_Type = EnableState
_AcuInsert_Object = MibScalar
acuInsert = _AcuInsert_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 5, 1, 2),
    _AcuInsert_Type()
)
acuInsert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acuInsert.setStatus("current")
_AcuCtlTable_Object = MibTable
acuCtlTable = _AcuCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 5, 2)
)
if mibBuilder.loadTexts:
    acuCtlTable.setStatus("current")
_AcuCtlEntry_Object = MibTableRow
acuCtlEntry = _AcuCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 5, 2, 1)
)
acuCtlEntry.setIndexNames(
    (0, "HAWK-I2-MIB", "acuNumber"),
)
if mibBuilder.loadTexts:
    acuCtlEntry.setStatus("current")


class _AcuNumber_Type(Integer32):
    """Custom type acuNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_AcuNumber_Type.__name__ = "Integer32"
_AcuNumber_Object = MibTableColumn
acuNumber = _AcuNumber_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 5, 2, 1, 1),
    _AcuNumber_Type()
)
acuNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acuNumber.setStatus("current")
_AcuCtlRS_Type = RowStatus
_AcuCtlRS_Object = MibTableColumn
acuCtlRS = _AcuCtlRS_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 5, 2, 1, 2),
    _AcuCtlRS_Type()
)
acuCtlRS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acuCtlRS.setStatus("current")


class _AcuManufacturer_Type(DisplayString):
    """Custom type acuManufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_AcuManufacturer_Type.__name__ = "DisplayString"
_AcuManufacturer_Object = MibTableColumn
acuManufacturer = _AcuManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 5, 2, 1, 3),
    _AcuManufacturer_Type()
)
acuManufacturer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acuManufacturer.setStatus("current")


class _AcuName_Type(DisplayString):
    """Custom type acuName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_AcuName_Type.__name__ = "DisplayString"
_AcuName_Object = MibTableColumn
acuName = _AcuName_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 5, 2, 1, 4),
    _AcuName_Type()
)
acuName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acuName.setStatus("current")
_AcuDoorLatchTimeOut_Type = Unsigned32
_AcuDoorLatchTimeOut_Object = MibTableColumn
acuDoorLatchTimeOut = _AcuDoorLatchTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 5, 2, 1, 5),
    _AcuDoorLatchTimeOut_Type()
)
acuDoorLatchTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acuDoorLatchTimeOut.setStatus("current")


class _AcuRtnToStndbyTimeOut_Type(Integer32):
    """Custom type acuRtnToStndbyTimeOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_AcuRtnToStndbyTimeOut_Type.__name__ = "Integer32"
_AcuRtnToStndbyTimeOut_Object = MibTableColumn
acuRtnToStndbyTimeOut = _AcuRtnToStndbyTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 5, 2, 1, 6),
    _AcuRtnToStndbyTimeOut_Type()
)
acuRtnToStndbyTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acuRtnToStndbyTimeOut.setStatus("current")
_AcuEntryCodeValid_Type = TruthValue
_AcuEntryCodeValid_Object = MibTableColumn
acuEntryCodeValid = _AcuEntryCodeValid_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 5, 2, 1, 7),
    _AcuEntryCodeValid_Type()
)
acuEntryCodeValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acuEntryCodeValid.setStatus("current")


class _AcuDoorOpenTimeOut_Type(Integer32):
    """Custom type acuDoorOpenTimeOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_AcuDoorOpenTimeOut_Type.__name__ = "Integer32"
_AcuDoorOpenTimeOut_Object = MibTableColumn
acuDoorOpenTimeOut = _AcuDoorOpenTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 5, 2, 1, 8),
    _AcuDoorOpenTimeOut_Type()
)
acuDoorOpenTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acuDoorOpenTimeOut.setStatus("current")
_AcuRemoteDoorOpen_Type = TruthValue
_AcuRemoteDoorOpen_Object = MibTableColumn
acuRemoteDoorOpen = _AcuRemoteDoorOpen_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 5, 2, 1, 9),
    _AcuRemoteDoorOpen_Type()
)
acuRemoteDoorOpen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acuRemoteDoorOpen.setStatus("current")


class _AcuInUseTrapEn_Type(Integer32):
    """Custom type acuInUseTrapEn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("critical", 1),
          ("warning", 2),
          ("information", 3),
          ("disabled", 255))
    )


_AcuInUseTrapEn_Type.__name__ = "Integer32"
_AcuInUseTrapEn_Object = MibTableColumn
acuInUseTrapEn = _AcuInUseTrapEn_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 5, 2, 1, 10),
    _AcuInUseTrapEn_Type()
)
acuInUseTrapEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acuInUseTrapEn.setStatus("current")
_Access_ObjectIdentity = ObjectIdentity
access = _Access_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 6)
)
_AccUserCtl_ObjectIdentity = ObjectIdentity
accUserCtl = _AccUserCtl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 6, 1)
)
_AccUserInstance_Type = Unsigned32
_AccUserInstance_Object = MibScalar
accUserInstance = _AccUserInstance_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 6, 1, 1),
    _AccUserInstance_Type()
)
accUserInstance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accUserInstance.setStatus("current")
_AccUserTable_Object = MibTable
accUserTable = _AccUserTable_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 6, 1, 2)
)
if mibBuilder.loadTexts:
    accUserTable.setStatus("current")
_AccUserEntry_Object = MibTableRow
accUserEntry = _AccUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 6, 1, 2, 1)
)
accUserEntry.setIndexNames(
    (0, "HAWK-I2-MIB", "accUserNumber"),
)
if mibBuilder.loadTexts:
    accUserEntry.setStatus("current")


class _AccUserNumber_Type(Integer32):
    """Custom type accUserNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_AccUserNumber_Type.__name__ = "Integer32"
_AccUserNumber_Object = MibTableColumn
accUserNumber = _AccUserNumber_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 6, 1, 2, 1, 1),
    _AccUserNumber_Type()
)
accUserNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accUserNumber.setStatus("current")
_AccUserRS_Type = RowStatus
_AccUserRS_Object = MibTableColumn
accUserRS = _AccUserRS_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 6, 1, 2, 1, 2),
    _AccUserRS_Type()
)
accUserRS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accUserRS.setStatus("current")


class _AccUserName_Type(DisplayString):
    """Custom type accUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_AccUserName_Type.__name__ = "DisplayString"
_AccUserName_Object = MibTableColumn
accUserName = _AccUserName_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 6, 1, 2, 1, 3),
    _AccUserName_Type()
)
accUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accUserName.setStatus("current")


class _AccUserCode_Type(OctetString):
    """Custom type accUserCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_AccUserCode_Type.__name__ = "OctetString"
_AccUserCode_Object = MibTableColumn
accUserCode = _AccUserCode_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 6, 1, 2, 1, 4),
    _AccUserCode_Type()
)
accUserCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accUserCode.setStatus("current")


class _AccUserPrivileges_Type(DisplayString):
    """Custom type accUserPrivileges based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_AccUserPrivileges_Type.__name__ = "DisplayString"
_AccUserPrivileges_Object = MibTableColumn
accUserPrivileges = _AccUserPrivileges_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 6, 1, 2, 1, 5),
    _AccUserPrivileges_Type()
)
accUserPrivileges.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accUserPrivileges.setStatus("current")
_AccUserExpires_Type = DisplayString
_AccUserExpires_Object = MibTableColumn
accUserExpires = _AccUserExpires_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 6, 1, 2, 1, 6),
    _AccUserExpires_Type()
)
accUserExpires.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accUserExpires.setStatus("current")
_AccUserSetup_Type = OctetString
_AccUserSetup_Object = MibScalar
accUserSetup = _AccUserSetup_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 6, 1, 3),
    _AccUserSetup_Type()
)
accUserSetup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accUserSetup.setStatus("current")
_Pdus_ObjectIdentity = ObjectIdentity
pdus = _Pdus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7)
)
_PduCommon_ObjectIdentity = ObjectIdentity
pduCommon = _PduCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 1)
)
_PdusEnable_ObjectIdentity = ObjectIdentity
pdusEnable = _PdusEnable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 1, 1)
)


class _PduSelect_Type(Integer32):
    """Custom type pduSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_PduSelect_Type.__name__ = "Integer32"
_PduSelect_Object = MibScalar
pduSelect = _PduSelect_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 1, 1, 1),
    _PduSelect_Type()
)
pduSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduSelect.setStatus("current")
_PduInsert_Type = EnableState
_PduInsert_Object = MibScalar
pduInsert = _PduInsert_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 1, 1, 2),
    _PduInsert_Type()
)
pduInsert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduInsert.setStatus("current")
_PduTable_Object = MibTable
pduTable = _PduTable_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 1, 2)
)
if mibBuilder.loadTexts:
    pduTable.setStatus("current")
_PduEntry_Object = MibTableRow
pduEntry = _PduEntry_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 1, 2, 1)
)
pduEntry.setIndexNames(
    (0, "HAWK-I2-MIB", "pduNumber"),
)
if mibBuilder.loadTexts:
    pduEntry.setStatus("current")


class _PduNumber_Type(Integer32):
    """Custom type pduNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_PduNumber_Type.__name__ = "Integer32"
_PduNumber_Object = MibTableColumn
pduNumber = _PduNumber_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 1, 2, 1, 1),
    _PduNumber_Type()
)
pduNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduNumber.setStatus("current")
_PduRS_Type = RowStatus
_PduRS_Object = MibTableColumn
pduRS = _PduRS_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 1, 2, 1, 2),
    _PduRS_Type()
)
pduRS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduRS.setStatus("current")


class _PduName_Type(DisplayString):
    """Custom type pduName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_PduName_Type.__name__ = "DisplayString"
_PduName_Object = MibTableColumn
pduName = _PduName_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 1, 2, 1, 3),
    _PduName_Type()
)
pduName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduName.setStatus("current")
_PduOutEn_Type = TruthValue
_PduOutEn_Object = MibTableColumn
pduOutEn = _PduOutEn_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 1, 2, 1, 4),
    _PduOutEn_Type()
)
pduOutEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduOutEn.setStatus("current")
_PduMonEn_Type = TruthValue
_PduMonEn_Object = MibTableColumn
pduMonEn = _PduMonEn_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 1, 2, 1, 5),
    _PduMonEn_Type()
)
pduMonEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduMonEn.setStatus("current")


class _PduCommsFail_Type(Integer32):
    """Custom type pduCommsFail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("commsGood", 1),
          ("commsFailed", 2),
          ("commsBadData", 3))
    )


_PduCommsFail_Type.__name__ = "Integer32"
_PduCommsFail_Object = MibTableColumn
pduCommsFail = _PduCommsFail_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 1, 2, 1, 6),
    _PduCommsFail_Type()
)
pduCommsFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduCommsFail.setStatus("current")
_PduOutlets_ObjectIdentity = ObjectIdentity
pduOutlets = _PduOutlets_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 2)
)
_PduOutAll_ObjectIdentity = ObjectIdentity
pduOutAll = _PduOutAll_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 2, 1)
)


class _PduOutCycleAll_Type(Integer32):
    """Custom type pduOutCycleAll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_PduOutCycleAll_Type.__name__ = "Integer32"
_PduOutCycleAll_Object = MibScalar
pduOutCycleAll = _PduOutCycleAll_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 2, 1, 1),
    _PduOutCycleAll_Type()
)
pduOutCycleAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduOutCycleAll.setStatus("current")


class _PduOutCycleAllPwd_Type(DisplayString):
    """Custom type pduOutCycleAllPwd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_PduOutCycleAllPwd_Type.__name__ = "DisplayString"
_PduOutCycleAllPwd_Object = MibScalar
pduOutCycleAllPwd = _PduOutCycleAllPwd_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 2, 1, 2),
    _PduOutCycleAllPwd_Type()
)
pduOutCycleAllPwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduOutCycleAllPwd.setStatus("current")
_PduOutCycleAllAbort_Type = Unsigned32
_PduOutCycleAllAbort_Object = MibScalar
pduOutCycleAllAbort = _PduOutCycleAllAbort_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 2, 1, 3),
    _PduOutCycleAllAbort_Type()
)
pduOutCycleAllAbort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduOutCycleAllAbort.setStatus("current")
_PduOutGlobalCycleDelay_Type = Unsigned32
_PduOutGlobalCycleDelay_Object = MibScalar
pduOutGlobalCycleDelay = _PduOutGlobalCycleDelay_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 2, 1, 4),
    _PduOutGlobalCycleDelay_Type()
)
pduOutGlobalCycleDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduOutGlobalCycleDelay.setStatus("current")
_PduOutGlobalRebootTime_Type = Unsigned32
_PduOutGlobalRebootTime_Object = MibScalar
pduOutGlobalRebootTime = _PduOutGlobalRebootTime_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 2, 1, 5),
    _PduOutGlobalRebootTime_Type()
)
pduOutGlobalRebootTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduOutGlobalRebootTime.setStatus("current")
_PduOutGlobalCycleAbortTime_Type = Unsigned32
_PduOutGlobalCycleAbortTime_Object = MibScalar
pduOutGlobalCycleAbortTime = _PduOutGlobalCycleAbortTime_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 2, 1, 6),
    _PduOutGlobalCycleAbortTime_Type()
)
pduOutGlobalCycleAbortTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduOutGlobalCycleAbortTime.setStatus("current")
_PduOutCmnTable_Object = MibTable
pduOutCmnTable = _PduOutCmnTable_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 2, 2)
)
if mibBuilder.loadTexts:
    pduOutCmnTable.setStatus("current")
_PduOutCmnEntry_Object = MibTableRow
pduOutCmnEntry = _PduOutCmnEntry_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 2, 2, 1)
)
pduOutCmnEntry.setIndexNames(
    (0, "HAWK-I2-MIB", "pduOutCmnPduNumber"),
)
if mibBuilder.loadTexts:
    pduOutCmnEntry.setStatus("current")


class _PduOutCmnPduNumber_Type(Integer32):
    """Custom type pduOutCmnPduNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_PduOutCmnPduNumber_Type.__name__ = "Integer32"
_PduOutCmnPduNumber_Object = MibTableColumn
pduOutCmnPduNumber = _PduOutCmnPduNumber_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 2, 2, 1, 1),
    _PduOutCmnPduNumber_Type()
)
pduOutCmnPduNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutCmnPduNumber.setStatus("current")
_PduOutCmnRS_Type = RowStatus
_PduOutCmnRS_Object = MibTableColumn
pduOutCmnRS = _PduOutCmnRS_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 2, 2, 1, 2),
    _PduOutCmnRS_Type()
)
pduOutCmnRS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutCmnRS.setStatus("current")


class _PduNumOfOutlets_Type(Integer32):
    """Custom type pduNumOfOutlets based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_PduNumOfOutlets_Type.__name__ = "Integer32"
_PduNumOfOutlets_Object = MibTableColumn
pduNumOfOutlets = _PduNumOfOutlets_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 2, 2, 1, 3),
    _PduNumOfOutlets_Type()
)
pduNumOfOutlets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduNumOfOutlets.setStatus("current")


class _PduOutCycle_Type(Integer32):
    """Custom type pduOutCycle based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_PduOutCycle_Type.__name__ = "Integer32"
_PduOutCycle_Object = MibTableColumn
pduOutCycle = _PduOutCycle_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 2, 2, 1, 4),
    _PduOutCycle_Type()
)
pduOutCycle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduOutCycle.setStatus("current")


class _PduOutCyclePwd_Type(DisplayString):
    """Custom type pduOutCyclePwd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_PduOutCyclePwd_Type.__name__ = "DisplayString"
_PduOutCyclePwd_Object = MibTableColumn
pduOutCyclePwd = _PduOutCyclePwd_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 2, 2, 1, 5),
    _PduOutCyclePwd_Type()
)
pduOutCyclePwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduOutCyclePwd.setStatus("current")
_PduOutCycleAbortTask_Type = Unsigned32
_PduOutCycleAbortTask_Object = MibTableColumn
pduOutCycleAbortTask = _PduOutCycleAbortTask_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 2, 2, 1, 6),
    _PduOutCycleAbortTask_Type()
)
pduOutCycleAbortTask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduOutCycleAbortTask.setStatus("current")
_PduOutCycleAbortTime_Type = Unsigned32
_PduOutCycleAbortTime_Object = MibTableColumn
pduOutCycleAbortTime = _PduOutCycleAbortTime_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 2, 2, 1, 7),
    _PduOutCycleAbortTime_Type()
)
pduOutCycleAbortTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduOutCycleAbortTime.setStatus("current")
_PduOutTable_Object = MibTable
pduOutTable = _PduOutTable_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 2, 3)
)
if mibBuilder.loadTexts:
    pduOutTable.setStatus("current")
_PduOutEntry_Object = MibTableRow
pduOutEntry = _PduOutEntry_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 2, 3, 1)
)
pduOutEntry.setIndexNames(
    (0, "HAWK-I2-MIB", "pduOutPduNumber"),
    (0, "HAWK-I2-MIB", "pduOutNumber"),
)
if mibBuilder.loadTexts:
    pduOutEntry.setStatus("current")


class _PduOutPduNumber_Type(Integer32):
    """Custom type pduOutPduNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_PduOutPduNumber_Type.__name__ = "Integer32"
_PduOutPduNumber_Object = MibTableColumn
pduOutPduNumber = _PduOutPduNumber_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 2, 3, 1, 1),
    _PduOutPduNumber_Type()
)
pduOutPduNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutPduNumber.setStatus("current")


class _PduOutNumber_Type(Integer32):
    """Custom type pduOutNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_PduOutNumber_Type.__name__ = "Integer32"
_PduOutNumber_Object = MibTableColumn
pduOutNumber = _PduOutNumber_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 2, 3, 1, 2),
    _PduOutNumber_Type()
)
pduOutNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutNumber.setStatus("current")
_PduOutRS_Type = RowStatus
_PduOutRS_Object = MibTableColumn
pduOutRS = _PduOutRS_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 2, 3, 1, 3),
    _PduOutRS_Type()
)
pduOutRS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutRS.setStatus("current")


class _PduOutName_Type(DisplayString):
    """Custom type pduOutName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_PduOutName_Type.__name__ = "DisplayString"
_PduOutName_Object = MibTableColumn
pduOutName = _PduOutName_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 2, 3, 1, 4),
    _PduOutName_Type()
)
pduOutName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduOutName.setStatus("current")


class _PduOutOn_Type(Integer32):
    """Custom type pduOutOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2),
          ("reboot", 3))
    )


_PduOutOn_Type.__name__ = "Integer32"
_PduOutOn_Object = MibTableColumn
pduOutOn = _PduOutOn_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 2, 3, 1, 5),
    _PduOutOn_Type()
)
pduOutOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduOutOn.setStatus("current")


class _PduOutPwd_Type(DisplayString):
    """Custom type pduOutPwd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_PduOutPwd_Type.__name__ = "DisplayString"
_PduOutPwd_Object = MibTableColumn
pduOutPwd = _PduOutPwd_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 2, 3, 1, 6),
    _PduOutPwd_Type()
)
pduOutPwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduOutPwd.setStatus("current")
_PduOutCycleDelay_Type = Unsigned32
_PduOutCycleDelay_Object = MibTableColumn
pduOutCycleDelay = _PduOutCycleDelay_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 2, 3, 1, 7),
    _PduOutCycleDelay_Type()
)
pduOutCycleDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutCycleDelay.setStatus("current")
_PduOutRebootPeriod_Type = Unsigned32
_PduOutRebootPeriod_Object = MibTableColumn
pduOutRebootPeriod = _PduOutRebootPeriod_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 2, 3, 1, 8),
    _PduOutRebootPeriod_Type()
)
pduOutRebootPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutRebootPeriod.setStatus("current")
_PduMonitor_ObjectIdentity = ObjectIdentity
pduMonitor = _PduMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3)
)
_PduMonTable_Object = MibTable
pduMonTable = _PduMonTable_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 1)
)
if mibBuilder.loadTexts:
    pduMonTable.setStatus("current")
_PduMonEntry_Object = MibTableRow
pduMonEntry = _PduMonEntry_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 1, 1)
)
pduMonEntry.setIndexNames(
    (0, "HAWK-I2-MIB", "pduMonPduNumber"),
)
if mibBuilder.loadTexts:
    pduMonEntry.setStatus("current")


class _PduMonPduNumber_Type(Integer32):
    """Custom type pduMonPduNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_PduMonPduNumber_Type.__name__ = "Integer32"
_PduMonPduNumber_Object = MibTableColumn
pduMonPduNumber = _PduMonPduNumber_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 1, 1, 1),
    _PduMonPduNumber_Type()
)
pduMonPduNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduMonPduNumber.setStatus("current")
_PduMonRS_Type = RowStatus
_PduMonRS_Object = MibTableColumn
pduMonRS = _PduMonRS_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 1, 1, 2),
    _PduMonRS_Type()
)
pduMonRS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduMonRS.setStatus("current")


class _PduRMSVoltsValue_Type(Integer32):
    """Custom type pduRMSVoltsValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_PduRMSVoltsValue_Type.__name__ = "Integer32"
_PduRMSVoltsValue_Object = MibTableColumn
pduRMSVoltsValue = _PduRMSVoltsValue_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 1, 1, 3),
    _PduRMSVoltsValue_Type()
)
pduRMSVoltsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduRMSVoltsValue.setStatus("current")


class _PduRMSAmpsValue_Type(Integer32):
    """Custom type pduRMSAmpsValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_PduRMSAmpsValue_Type.__name__ = "Integer32"
_PduRMSAmpsValue_Object = MibTableColumn
pduRMSAmpsValue = _PduRMSAmpsValue_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 1, 1, 4),
    _PduRMSAmpsValue_Type()
)
pduRMSAmpsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduRMSAmpsValue.setStatus("current")


class _PduTotalEnergyValue_Type(Integer32):
    """Custom type pduTotalEnergyValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999999),
    )


_PduTotalEnergyValue_Type.__name__ = "Integer32"
_PduTotalEnergyValue_Object = MibTableColumn
pduTotalEnergyValue = _PduTotalEnergyValue_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 1, 1, 5),
    _PduTotalEnergyValue_Type()
)
pduTotalEnergyValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduTotalEnergyValue.setStatus("current")


class _PduMeanKVAValue_Type(Integer32):
    """Custom type pduMeanKVAValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_PduMeanKVAValue_Type.__name__ = "Integer32"
_PduMeanKVAValue_Object = MibTableColumn
pduMeanKVAValue = _PduMeanKVAValue_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 1, 1, 6),
    _PduMeanKVAValue_Type()
)
pduMeanKVAValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduMeanKVAValue.setStatus("current")


class _PduMeanKWattsValue_Type(Integer32):
    """Custom type pduMeanKWattsValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_PduMeanKWattsValue_Type.__name__ = "Integer32"
_PduMeanKWattsValue_Object = MibTableColumn
pduMeanKWattsValue = _PduMeanKWattsValue_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 1, 1, 7),
    _PduMeanKWattsValue_Type()
)
pduMeanKWattsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduMeanKWattsValue.setStatus("current")


class _PduPwrFactorValue_Type(Integer32):
    """Custom type pduPwrFactorValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PduPwrFactorValue_Type.__name__ = "Integer32"
_PduPwrFactorValue_Object = MibTableColumn
pduPwrFactorValue = _PduPwrFactorValue_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 1, 1, 8),
    _PduPwrFactorValue_Type()
)
pduPwrFactorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduPwrFactorValue.setStatus("current")
_PduTrapThreshTable_Object = MibTable
pduTrapThreshTable = _PduTrapThreshTable_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 2)
)
if mibBuilder.loadTexts:
    pduTrapThreshTable.setStatus("current")
_PduTrapThreshEntry_Object = MibTableRow
pduTrapThreshEntry = _PduTrapThreshEntry_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 2, 1)
)
pduTrapThreshEntry.setIndexNames(
    (0, "HAWK-I2-MIB", "pduTrapThreshPduNumber"),
)
if mibBuilder.loadTexts:
    pduTrapThreshEntry.setStatus("current")


class _PduTrapThreshPduNumber_Type(Integer32):
    """Custom type pduTrapThreshPduNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_PduTrapThreshPduNumber_Type.__name__ = "Integer32"
_PduTrapThreshPduNumber_Object = MibTableColumn
pduTrapThreshPduNumber = _PduTrapThreshPduNumber_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 2, 1, 1),
    _PduTrapThreshPduNumber_Type()
)
pduTrapThreshPduNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduTrapThreshPduNumber.setStatus("current")
_PduTrapThreshRS_Type = RowStatus
_PduTrapThreshRS_Object = MibTableColumn
pduTrapThreshRS = _PduTrapThreshRS_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 2, 1, 2),
    _PduTrapThreshRS_Type()
)
pduTrapThreshRS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduTrapThreshRS.setStatus("current")


class _PduRMSVoltsUCL_Type(Integer32):
    """Custom type pduRMSVoltsUCL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_PduRMSVoltsUCL_Type.__name__ = "Integer32"
_PduRMSVoltsUCL_Object = MibTableColumn
pduRMSVoltsUCL = _PduRMSVoltsUCL_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 2, 1, 3),
    _PduRMSVoltsUCL_Type()
)
pduRMSVoltsUCL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduRMSVoltsUCL.setStatus("current")


class _PduRMSVoltsUWL_Type(Integer32):
    """Custom type pduRMSVoltsUWL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_PduRMSVoltsUWL_Type.__name__ = "Integer32"
_PduRMSVoltsUWL_Object = MibTableColumn
pduRMSVoltsUWL = _PduRMSVoltsUWL_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 2, 1, 4),
    _PduRMSVoltsUWL_Type()
)
pduRMSVoltsUWL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduRMSVoltsUWL.setStatus("current")


class _PduRMSVoltsLWL_Type(Integer32):
    """Custom type pduRMSVoltsLWL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_PduRMSVoltsLWL_Type.__name__ = "Integer32"
_PduRMSVoltsLWL_Object = MibTableColumn
pduRMSVoltsLWL = _PduRMSVoltsLWL_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 2, 1, 5),
    _PduRMSVoltsLWL_Type()
)
pduRMSVoltsLWL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduRMSVoltsLWL.setStatus("current")


class _PduRMSVoltsLCL_Type(Integer32):
    """Custom type pduRMSVoltsLCL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_PduRMSVoltsLCL_Type.__name__ = "Integer32"
_PduRMSVoltsLCL_Object = MibTableColumn
pduRMSVoltsLCL = _PduRMSVoltsLCL_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 2, 1, 6),
    _PduRMSVoltsLCL_Type()
)
pduRMSVoltsLCL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduRMSVoltsLCL.setStatus("current")


class _PduRMSAmpsUCL_Type(Integer32):
    """Custom type pduRMSAmpsUCL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_PduRMSAmpsUCL_Type.__name__ = "Integer32"
_PduRMSAmpsUCL_Object = MibTableColumn
pduRMSAmpsUCL = _PduRMSAmpsUCL_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 2, 1, 7),
    _PduRMSAmpsUCL_Type()
)
pduRMSAmpsUCL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduRMSAmpsUCL.setStatus("current")


class _PduRMSAmpsUWL_Type(Integer32):
    """Custom type pduRMSAmpsUWL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_PduRMSAmpsUWL_Type.__name__ = "Integer32"
_PduRMSAmpsUWL_Object = MibTableColumn
pduRMSAmpsUWL = _PduRMSAmpsUWL_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 2, 1, 8),
    _PduRMSAmpsUWL_Type()
)
pduRMSAmpsUWL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduRMSAmpsUWL.setStatus("current")


class _PduRMSAmpsLWL_Type(Integer32):
    """Custom type pduRMSAmpsLWL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_PduRMSAmpsLWL_Type.__name__ = "Integer32"
_PduRMSAmpsLWL_Object = MibTableColumn
pduRMSAmpsLWL = _PduRMSAmpsLWL_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 2, 1, 9),
    _PduRMSAmpsLWL_Type()
)
pduRMSAmpsLWL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduRMSAmpsLWL.setStatus("current")


class _PduRMSAmpsLCL_Type(Integer32):
    """Custom type pduRMSAmpsLCL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_PduRMSAmpsLCL_Type.__name__ = "Integer32"
_PduRMSAmpsLCL_Object = MibTableColumn
pduRMSAmpsLCL = _PduRMSAmpsLCL_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 2, 1, 10),
    _PduRMSAmpsLCL_Type()
)
pduRMSAmpsLCL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduRMSAmpsLCL.setStatus("current")


class _PduEnergyUCL_Type(Integer32):
    """Custom type pduEnergyUCL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999999),
    )


_PduEnergyUCL_Type.__name__ = "Integer32"
_PduEnergyUCL_Object = MibTableColumn
pduEnergyUCL = _PduEnergyUCL_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 2, 1, 11),
    _PduEnergyUCL_Type()
)
pduEnergyUCL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduEnergyUCL.setStatus("current")


class _PduEnergyUWL_Type(Integer32):
    """Custom type pduEnergyUWL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999999),
    )


_PduEnergyUWL_Type.__name__ = "Integer32"
_PduEnergyUWL_Object = MibTableColumn
pduEnergyUWL = _PduEnergyUWL_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 2, 1, 12),
    _PduEnergyUWL_Type()
)
pduEnergyUWL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduEnergyUWL.setStatus("current")


class _PduMeanKVAUCL_Type(Integer32):
    """Custom type pduMeanKVAUCL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_PduMeanKVAUCL_Type.__name__ = "Integer32"
_PduMeanKVAUCL_Object = MibTableColumn
pduMeanKVAUCL = _PduMeanKVAUCL_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 2, 1, 13),
    _PduMeanKVAUCL_Type()
)
pduMeanKVAUCL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduMeanKVAUCL.setStatus("current")


class _PduMeanKVAUWL_Type(Integer32):
    """Custom type pduMeanKVAUWL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_PduMeanKVAUWL_Type.__name__ = "Integer32"
_PduMeanKVAUWL_Object = MibTableColumn
pduMeanKVAUWL = _PduMeanKVAUWL_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 2, 1, 14),
    _PduMeanKVAUWL_Type()
)
pduMeanKVAUWL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduMeanKVAUWL.setStatus("current")


class _PduMeanKVALWL_Type(Integer32):
    """Custom type pduMeanKVALWL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_PduMeanKVALWL_Type.__name__ = "Integer32"
_PduMeanKVALWL_Object = MibTableColumn
pduMeanKVALWL = _PduMeanKVALWL_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 2, 1, 15),
    _PduMeanKVALWL_Type()
)
pduMeanKVALWL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduMeanKVALWL.setStatus("current")


class _PduMeanKVALCL_Type(Integer32):
    """Custom type pduMeanKVALCL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_PduMeanKVALCL_Type.__name__ = "Integer32"
_PduMeanKVALCL_Object = MibTableColumn
pduMeanKVALCL = _PduMeanKVALCL_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 2, 1, 16),
    _PduMeanKVALCL_Type()
)
pduMeanKVALCL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduMeanKVALCL.setStatus("current")


class _PduMeanKWattsUCL_Type(Integer32):
    """Custom type pduMeanKWattsUCL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_PduMeanKWattsUCL_Type.__name__ = "Integer32"
_PduMeanKWattsUCL_Object = MibTableColumn
pduMeanKWattsUCL = _PduMeanKWattsUCL_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 2, 1, 17),
    _PduMeanKWattsUCL_Type()
)
pduMeanKWattsUCL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduMeanKWattsUCL.setStatus("current")


class _PduMeanKWattsUWL_Type(Integer32):
    """Custom type pduMeanKWattsUWL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_PduMeanKWattsUWL_Type.__name__ = "Integer32"
_PduMeanKWattsUWL_Object = MibTableColumn
pduMeanKWattsUWL = _PduMeanKWattsUWL_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 2, 1, 18),
    _PduMeanKWattsUWL_Type()
)
pduMeanKWattsUWL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduMeanKWattsUWL.setStatus("current")


class _PduMeanKWattsLWL_Type(Integer32):
    """Custom type pduMeanKWattsLWL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_PduMeanKWattsLWL_Type.__name__ = "Integer32"
_PduMeanKWattsLWL_Object = MibTableColumn
pduMeanKWattsLWL = _PduMeanKWattsLWL_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 2, 1, 19),
    _PduMeanKWattsLWL_Type()
)
pduMeanKWattsLWL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduMeanKWattsLWL.setStatus("current")


class _PduMeanKWattsLCL_Type(Integer32):
    """Custom type pduMeanKWattsLCL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_PduMeanKWattsLCL_Type.__name__ = "Integer32"
_PduMeanKWattsLCL_Object = MibTableColumn
pduMeanKWattsLCL = _PduMeanKWattsLCL_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 2, 1, 20),
    _PduMeanKWattsLCL_Type()
)
pduMeanKWattsLCL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduMeanKWattsLCL.setStatus("current")


class _PduPwrFactorUCL_Type(Integer32):
    """Custom type pduPwrFactorUCL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PduPwrFactorUCL_Type.__name__ = "Integer32"
_PduPwrFactorUCL_Object = MibTableColumn
pduPwrFactorUCL = _PduPwrFactorUCL_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 2, 1, 21),
    _PduPwrFactorUCL_Type()
)
pduPwrFactorUCL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduPwrFactorUCL.setStatus("current")


class _PduPwrFactorUWL_Type(Integer32):
    """Custom type pduPwrFactorUWL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PduPwrFactorUWL_Type.__name__ = "Integer32"
_PduPwrFactorUWL_Object = MibTableColumn
pduPwrFactorUWL = _PduPwrFactorUWL_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 2, 1, 22),
    _PduPwrFactorUWL_Type()
)
pduPwrFactorUWL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduPwrFactorUWL.setStatus("current")


class _PduPwrFactorLWL_Type(Integer32):
    """Custom type pduPwrFactorLWL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PduPwrFactorLWL_Type.__name__ = "Integer32"
_PduPwrFactorLWL_Object = MibTableColumn
pduPwrFactorLWL = _PduPwrFactorLWL_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 2, 1, 23),
    _PduPwrFactorLWL_Type()
)
pduPwrFactorLWL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduPwrFactorLWL.setStatus("current")


class _PduPwrFactorLCL_Type(Integer32):
    """Custom type pduPwrFactorLCL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PduPwrFactorLCL_Type.__name__ = "Integer32"
_PduPwrFactorLCL_Object = MibTableColumn
pduPwrFactorLCL = _PduPwrFactorLCL_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 2, 1, 24),
    _PduPwrFactorLCL_Type()
)
pduPwrFactorLCL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduPwrFactorLCL.setStatus("current")
_PduTrapEnTable_Object = MibTable
pduTrapEnTable = _PduTrapEnTable_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 3)
)
if mibBuilder.loadTexts:
    pduTrapEnTable.setStatus("current")
_PduTrapEnEntry_Object = MibTableRow
pduTrapEnEntry = _PduTrapEnEntry_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 3, 1)
)
pduTrapEnEntry.setIndexNames(
    (0, "HAWK-I2-MIB", "pduTrapEnPduNumber"),
)
if mibBuilder.loadTexts:
    pduTrapEnEntry.setStatus("current")


class _PduTrapEnPduNumber_Type(Integer32):
    """Custom type pduTrapEnPduNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_PduTrapEnPduNumber_Type.__name__ = "Integer32"
_PduTrapEnPduNumber_Object = MibTableColumn
pduTrapEnPduNumber = _PduTrapEnPduNumber_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 3, 1, 1),
    _PduTrapEnPduNumber_Type()
)
pduTrapEnPduNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduTrapEnPduNumber.setStatus("current")
_PduTrapEnRS_Type = RowStatus
_PduTrapEnRS_Object = MibTableColumn
pduTrapEnRS = _PduTrapEnRS_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 3, 1, 2),
    _PduTrapEnRS_Type()
)
pduTrapEnRS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduTrapEnRS.setStatus("current")
_PduRMSVoltsUCLTrapEn_Type = TruthValue
_PduRMSVoltsUCLTrapEn_Object = MibTableColumn
pduRMSVoltsUCLTrapEn = _PduRMSVoltsUCLTrapEn_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 3, 1, 3),
    _PduRMSVoltsUCLTrapEn_Type()
)
pduRMSVoltsUCLTrapEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduRMSVoltsUCLTrapEn.setStatus("current")
_PduRMSVoltsUWLTrapEn_Type = TruthValue
_PduRMSVoltsUWLTrapEn_Object = MibTableColumn
pduRMSVoltsUWLTrapEn = _PduRMSVoltsUWLTrapEn_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 3, 1, 4),
    _PduRMSVoltsUWLTrapEn_Type()
)
pduRMSVoltsUWLTrapEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduRMSVoltsUWLTrapEn.setStatus("current")
_PduRMSVoltsLWLTrapEn_Type = TruthValue
_PduRMSVoltsLWLTrapEn_Object = MibTableColumn
pduRMSVoltsLWLTrapEn = _PduRMSVoltsLWLTrapEn_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 3, 1, 5),
    _PduRMSVoltsLWLTrapEn_Type()
)
pduRMSVoltsLWLTrapEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduRMSVoltsLWLTrapEn.setStatus("current")
_PduRMSVoltsLCLTrapEn_Type = TruthValue
_PduRMSVoltsLCLTrapEn_Object = MibTableColumn
pduRMSVoltsLCLTrapEn = _PduRMSVoltsLCLTrapEn_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 3, 1, 6),
    _PduRMSVoltsLCLTrapEn_Type()
)
pduRMSVoltsLCLTrapEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduRMSVoltsLCLTrapEn.setStatus("current")
_PduRMSAmpsUCLTrapEn_Type = TruthValue
_PduRMSAmpsUCLTrapEn_Object = MibTableColumn
pduRMSAmpsUCLTrapEn = _PduRMSAmpsUCLTrapEn_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 3, 1, 7),
    _PduRMSAmpsUCLTrapEn_Type()
)
pduRMSAmpsUCLTrapEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduRMSAmpsUCLTrapEn.setStatus("current")
_PduRMSAmpsUWLTrapEn_Type = TruthValue
_PduRMSAmpsUWLTrapEn_Object = MibTableColumn
pduRMSAmpsUWLTrapEn = _PduRMSAmpsUWLTrapEn_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 3, 1, 8),
    _PduRMSAmpsUWLTrapEn_Type()
)
pduRMSAmpsUWLTrapEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduRMSAmpsUWLTrapEn.setStatus("current")
_PduRMSAmpsLWLTrapEn_Type = TruthValue
_PduRMSAmpsLWLTrapEn_Object = MibTableColumn
pduRMSAmpsLWLTrapEn = _PduRMSAmpsLWLTrapEn_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 3, 1, 9),
    _PduRMSAmpsLWLTrapEn_Type()
)
pduRMSAmpsLWLTrapEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduRMSAmpsLWLTrapEn.setStatus("current")
_PduRMSAmpsLCLTrapEn_Type = TruthValue
_PduRMSAmpsLCLTrapEn_Object = MibTableColumn
pduRMSAmpsLCLTrapEn = _PduRMSAmpsLCLTrapEn_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 3, 1, 10),
    _PduRMSAmpsLCLTrapEn_Type()
)
pduRMSAmpsLCLTrapEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduRMSAmpsLCLTrapEn.setStatus("current")
_PduEnergyUCLTrapEn_Type = TruthValue
_PduEnergyUCLTrapEn_Object = MibTableColumn
pduEnergyUCLTrapEn = _PduEnergyUCLTrapEn_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 3, 1, 11),
    _PduEnergyUCLTrapEn_Type()
)
pduEnergyUCLTrapEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduEnergyUCLTrapEn.setStatus("current")
_PduEnergyUWLTrapEn_Type = TruthValue
_PduEnergyUWLTrapEn_Object = MibTableColumn
pduEnergyUWLTrapEn = _PduEnergyUWLTrapEn_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 3, 1, 12),
    _PduEnergyUWLTrapEn_Type()
)
pduEnergyUWLTrapEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduEnergyUWLTrapEn.setStatus("current")
_PduMeanKVAUCLTrapEn_Type = TruthValue
_PduMeanKVAUCLTrapEn_Object = MibTableColumn
pduMeanKVAUCLTrapEn = _PduMeanKVAUCLTrapEn_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 3, 1, 13),
    _PduMeanKVAUCLTrapEn_Type()
)
pduMeanKVAUCLTrapEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduMeanKVAUCLTrapEn.setStatus("current")
_PduMeanKVAUWLTrapEn_Type = TruthValue
_PduMeanKVAUWLTrapEn_Object = MibTableColumn
pduMeanKVAUWLTrapEn = _PduMeanKVAUWLTrapEn_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 3, 1, 14),
    _PduMeanKVAUWLTrapEn_Type()
)
pduMeanKVAUWLTrapEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduMeanKVAUWLTrapEn.setStatus("current")
_PduMeanKVALWLTrapEn_Type = TruthValue
_PduMeanKVALWLTrapEn_Object = MibTableColumn
pduMeanKVALWLTrapEn = _PduMeanKVALWLTrapEn_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 3, 1, 15),
    _PduMeanKVALWLTrapEn_Type()
)
pduMeanKVALWLTrapEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduMeanKVALWLTrapEn.setStatus("current")
_PduMeanKVALCLTrapEn_Type = TruthValue
_PduMeanKVALCLTrapEn_Object = MibTableColumn
pduMeanKVALCLTrapEn = _PduMeanKVALCLTrapEn_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 3, 1, 16),
    _PduMeanKVALCLTrapEn_Type()
)
pduMeanKVALCLTrapEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduMeanKVALCLTrapEn.setStatus("current")
_PduMeanKWattsUCLTrapEn_Type = TruthValue
_PduMeanKWattsUCLTrapEn_Object = MibTableColumn
pduMeanKWattsUCLTrapEn = _PduMeanKWattsUCLTrapEn_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 3, 1, 17),
    _PduMeanKWattsUCLTrapEn_Type()
)
pduMeanKWattsUCLTrapEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduMeanKWattsUCLTrapEn.setStatus("current")
_PduMeanKWattsUWLTrapEn_Type = TruthValue
_PduMeanKWattsUWLTrapEn_Object = MibTableColumn
pduMeanKWattsUWLTrapEn = _PduMeanKWattsUWLTrapEn_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 3, 1, 18),
    _PduMeanKWattsUWLTrapEn_Type()
)
pduMeanKWattsUWLTrapEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduMeanKWattsUWLTrapEn.setStatus("current")
_PduMeanKWattsLWLTrapEn_Type = TruthValue
_PduMeanKWattsLWLTrapEn_Object = MibTableColumn
pduMeanKWattsLWLTrapEn = _PduMeanKWattsLWLTrapEn_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 3, 1, 19),
    _PduMeanKWattsLWLTrapEn_Type()
)
pduMeanKWattsLWLTrapEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduMeanKWattsLWLTrapEn.setStatus("current")
_PduMeanKWattsLCLTrapEn_Type = TruthValue
_PduMeanKWattsLCLTrapEn_Object = MibTableColumn
pduMeanKWattsLCLTrapEn = _PduMeanKWattsLCLTrapEn_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 3, 1, 20),
    _PduMeanKWattsLCLTrapEn_Type()
)
pduMeanKWattsLCLTrapEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduMeanKWattsLCLTrapEn.setStatus("current")
_PduPwrFactorUCLTrapEn_Type = TruthValue
_PduPwrFactorUCLTrapEn_Object = MibTableColumn
pduPwrFactorUCLTrapEn = _PduPwrFactorUCLTrapEn_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 3, 1, 21),
    _PduPwrFactorUCLTrapEn_Type()
)
pduPwrFactorUCLTrapEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduPwrFactorUCLTrapEn.setStatus("current")
_PduPwrFactorUWLTrapEn_Type = TruthValue
_PduPwrFactorUWLTrapEn_Object = MibTableColumn
pduPwrFactorUWLTrapEn = _PduPwrFactorUWLTrapEn_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 3, 1, 22),
    _PduPwrFactorUWLTrapEn_Type()
)
pduPwrFactorUWLTrapEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduPwrFactorUWLTrapEn.setStatus("current")
_PduPwrFactorLWLTrapEn_Type = TruthValue
_PduPwrFactorLWLTrapEn_Object = MibTableColumn
pduPwrFactorLWLTrapEn = _PduPwrFactorLWLTrapEn_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 3, 1, 23),
    _PduPwrFactorLWLTrapEn_Type()
)
pduPwrFactorLWLTrapEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduPwrFactorLWLTrapEn.setStatus("current")
_PduPwrFactorLCLTrapEn_Type = TruthValue
_PduPwrFactorLCLTrapEn_Object = MibTableColumn
pduPwrFactorLCLTrapEn = _PduPwrFactorLCLTrapEn_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 3, 1, 24),
    _PduPwrFactorLCLTrapEn_Type()
)
pduPwrFactorLCLTrapEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduPwrFactorLCLTrapEn.setStatus("current")
_PduTrapPerTable_Object = MibTable
pduTrapPerTable = _PduTrapPerTable_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 4)
)
if mibBuilder.loadTexts:
    pduTrapPerTable.setStatus("current")
_PduTrapPerEntry_Object = MibTableRow
pduTrapPerEntry = _PduTrapPerEntry_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 4, 1)
)
pduTrapPerEntry.setIndexNames(
    (0, "HAWK-I2-MIB", "pduTrapPduNumber"),
)
if mibBuilder.loadTexts:
    pduTrapPerEntry.setStatus("current")


class _PduTrapPduNumber_Type(Integer32):
    """Custom type pduTrapPduNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_PduTrapPduNumber_Type.__name__ = "Integer32"
_PduTrapPduNumber_Object = MibTableColumn
pduTrapPduNumber = _PduTrapPduNumber_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 4, 1, 1),
    _PduTrapPduNumber_Type()
)
pduTrapPduNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduTrapPduNumber.setStatus("current")
_PduTrapPerRS_Type = RowStatus
_PduTrapPerRS_Object = MibTableColumn
pduTrapPerRS = _PduTrapPerRS_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 4, 1, 2),
    _PduTrapPerRS_Type()
)
pduTrapPerRS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduTrapPerRS.setStatus("current")


class _PduRMSVoltsUCLTrapPer_Type(Integer32):
    """Custom type pduRMSVoltsUCLTrapPer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 32000),
    )


_PduRMSVoltsUCLTrapPer_Type.__name__ = "Integer32"
_PduRMSVoltsUCLTrapPer_Object = MibTableColumn
pduRMSVoltsUCLTrapPer = _PduRMSVoltsUCLTrapPer_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 4, 1, 3),
    _PduRMSVoltsUCLTrapPer_Type()
)
pduRMSVoltsUCLTrapPer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduRMSVoltsUCLTrapPer.setStatus("current")


class _PduRMSVoltsUWLTrapPer_Type(Integer32):
    """Custom type pduRMSVoltsUWLTrapPer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 32000),
    )


_PduRMSVoltsUWLTrapPer_Type.__name__ = "Integer32"
_PduRMSVoltsUWLTrapPer_Object = MibTableColumn
pduRMSVoltsUWLTrapPer = _PduRMSVoltsUWLTrapPer_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 4, 1, 4),
    _PduRMSVoltsUWLTrapPer_Type()
)
pduRMSVoltsUWLTrapPer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduRMSVoltsUWLTrapPer.setStatus("current")


class _PduRMSVoltsLWLTrapPer_Type(Integer32):
    """Custom type pduRMSVoltsLWLTrapPer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 32000),
    )


_PduRMSVoltsLWLTrapPer_Type.__name__ = "Integer32"
_PduRMSVoltsLWLTrapPer_Object = MibTableColumn
pduRMSVoltsLWLTrapPer = _PduRMSVoltsLWLTrapPer_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 4, 1, 5),
    _PduRMSVoltsLWLTrapPer_Type()
)
pduRMSVoltsLWLTrapPer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduRMSVoltsLWLTrapPer.setStatus("current")


class _PduRMSVoltsLCLTrapPer_Type(Integer32):
    """Custom type pduRMSVoltsLCLTrapPer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 32000),
    )


_PduRMSVoltsLCLTrapPer_Type.__name__ = "Integer32"
_PduRMSVoltsLCLTrapPer_Object = MibTableColumn
pduRMSVoltsLCLTrapPer = _PduRMSVoltsLCLTrapPer_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 4, 1, 6),
    _PduRMSVoltsLCLTrapPer_Type()
)
pduRMSVoltsLCLTrapPer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduRMSVoltsLCLTrapPer.setStatus("current")


class _PduRMSAmpsUCLTrapPer_Type(Integer32):
    """Custom type pduRMSAmpsUCLTrapPer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 32000),
    )


_PduRMSAmpsUCLTrapPer_Type.__name__ = "Integer32"
_PduRMSAmpsUCLTrapPer_Object = MibTableColumn
pduRMSAmpsUCLTrapPer = _PduRMSAmpsUCLTrapPer_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 4, 1, 7),
    _PduRMSAmpsUCLTrapPer_Type()
)
pduRMSAmpsUCLTrapPer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduRMSAmpsUCLTrapPer.setStatus("current")


class _PduRMSAmpsUWLTrapPer_Type(Integer32):
    """Custom type pduRMSAmpsUWLTrapPer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 32000),
    )


_PduRMSAmpsUWLTrapPer_Type.__name__ = "Integer32"
_PduRMSAmpsUWLTrapPer_Object = MibTableColumn
pduRMSAmpsUWLTrapPer = _PduRMSAmpsUWLTrapPer_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 4, 1, 8),
    _PduRMSAmpsUWLTrapPer_Type()
)
pduRMSAmpsUWLTrapPer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduRMSAmpsUWLTrapPer.setStatus("current")


class _PduRMSAmpsLWLTrapPer_Type(Integer32):
    """Custom type pduRMSAmpsLWLTrapPer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 32000),
    )


_PduRMSAmpsLWLTrapPer_Type.__name__ = "Integer32"
_PduRMSAmpsLWLTrapPer_Object = MibTableColumn
pduRMSAmpsLWLTrapPer = _PduRMSAmpsLWLTrapPer_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 4, 1, 9),
    _PduRMSAmpsLWLTrapPer_Type()
)
pduRMSAmpsLWLTrapPer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduRMSAmpsLWLTrapPer.setStatus("current")


class _PduRMSAmpsLCLTrapPer_Type(Integer32):
    """Custom type pduRMSAmpsLCLTrapPer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 32000),
    )


_PduRMSAmpsLCLTrapPer_Type.__name__ = "Integer32"
_PduRMSAmpsLCLTrapPer_Object = MibTableColumn
pduRMSAmpsLCLTrapPer = _PduRMSAmpsLCLTrapPer_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 4, 1, 10),
    _PduRMSAmpsLCLTrapPer_Type()
)
pduRMSAmpsLCLTrapPer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduRMSAmpsLCLTrapPer.setStatus("current")


class _PduEnergyUCLTrapPer_Type(Integer32):
    """Custom type pduEnergyUCLTrapPer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 32000),
    )


_PduEnergyUCLTrapPer_Type.__name__ = "Integer32"
_PduEnergyUCLTrapPer_Object = MibTableColumn
pduEnergyUCLTrapPer = _PduEnergyUCLTrapPer_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 4, 1, 11),
    _PduEnergyUCLTrapPer_Type()
)
pduEnergyUCLTrapPer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduEnergyUCLTrapPer.setStatus("current")


class _PduEnergyUWLTrapPer_Type(Integer32):
    """Custom type pduEnergyUWLTrapPer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 32000),
    )


_PduEnergyUWLTrapPer_Type.__name__ = "Integer32"
_PduEnergyUWLTrapPer_Object = MibTableColumn
pduEnergyUWLTrapPer = _PduEnergyUWLTrapPer_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 4, 1, 12),
    _PduEnergyUWLTrapPer_Type()
)
pduEnergyUWLTrapPer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduEnergyUWLTrapPer.setStatus("current")


class _PduMeanKVAUCLTrapPer_Type(Integer32):
    """Custom type pduMeanKVAUCLTrapPer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 32000),
    )


_PduMeanKVAUCLTrapPer_Type.__name__ = "Integer32"
_PduMeanKVAUCLTrapPer_Object = MibTableColumn
pduMeanKVAUCLTrapPer = _PduMeanKVAUCLTrapPer_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 4, 1, 13),
    _PduMeanKVAUCLTrapPer_Type()
)
pduMeanKVAUCLTrapPer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduMeanKVAUCLTrapPer.setStatus("current")


class _PduMeanKVAUWLTrapPer_Type(Integer32):
    """Custom type pduMeanKVAUWLTrapPer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 32000),
    )


_PduMeanKVAUWLTrapPer_Type.__name__ = "Integer32"
_PduMeanKVAUWLTrapPer_Object = MibTableColumn
pduMeanKVAUWLTrapPer = _PduMeanKVAUWLTrapPer_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 4, 1, 14),
    _PduMeanKVAUWLTrapPer_Type()
)
pduMeanKVAUWLTrapPer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduMeanKVAUWLTrapPer.setStatus("current")


class _PduMeanKVALWLTrapPer_Type(Integer32):
    """Custom type pduMeanKVALWLTrapPer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 32000),
    )


_PduMeanKVALWLTrapPer_Type.__name__ = "Integer32"
_PduMeanKVALWLTrapPer_Object = MibTableColumn
pduMeanKVALWLTrapPer = _PduMeanKVALWLTrapPer_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 4, 1, 15),
    _PduMeanKVALWLTrapPer_Type()
)
pduMeanKVALWLTrapPer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduMeanKVALWLTrapPer.setStatus("current")


class _PduMeanKVALCLTrapPer_Type(Integer32):
    """Custom type pduMeanKVALCLTrapPer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 32000),
    )


_PduMeanKVALCLTrapPer_Type.__name__ = "Integer32"
_PduMeanKVALCLTrapPer_Object = MibTableColumn
pduMeanKVALCLTrapPer = _PduMeanKVALCLTrapPer_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 4, 1, 16),
    _PduMeanKVALCLTrapPer_Type()
)
pduMeanKVALCLTrapPer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduMeanKVALCLTrapPer.setStatus("current")


class _PduMeanKWattsUCLTrapPer_Type(Integer32):
    """Custom type pduMeanKWattsUCLTrapPer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 32000),
    )


_PduMeanKWattsUCLTrapPer_Type.__name__ = "Integer32"
_PduMeanKWattsUCLTrapPer_Object = MibTableColumn
pduMeanKWattsUCLTrapPer = _PduMeanKWattsUCLTrapPer_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 4, 1, 17),
    _PduMeanKWattsUCLTrapPer_Type()
)
pduMeanKWattsUCLTrapPer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduMeanKWattsUCLTrapPer.setStatus("current")


class _PduMeanKWattsUWLTrapPer_Type(Integer32):
    """Custom type pduMeanKWattsUWLTrapPer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 32000),
    )


_PduMeanKWattsUWLTrapPer_Type.__name__ = "Integer32"
_PduMeanKWattsUWLTrapPer_Object = MibTableColumn
pduMeanKWattsUWLTrapPer = _PduMeanKWattsUWLTrapPer_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 4, 1, 18),
    _PduMeanKWattsUWLTrapPer_Type()
)
pduMeanKWattsUWLTrapPer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduMeanKWattsUWLTrapPer.setStatus("current")


class _PduMeanKWattsLWLTrapPer_Type(Integer32):
    """Custom type pduMeanKWattsLWLTrapPer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 32000),
    )


_PduMeanKWattsLWLTrapPer_Type.__name__ = "Integer32"
_PduMeanKWattsLWLTrapPer_Object = MibTableColumn
pduMeanKWattsLWLTrapPer = _PduMeanKWattsLWLTrapPer_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 4, 1, 19),
    _PduMeanKWattsLWLTrapPer_Type()
)
pduMeanKWattsLWLTrapPer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduMeanKWattsLWLTrapPer.setStatus("current")


class _PduMeanKWattsLCLTrapPer_Type(Integer32):
    """Custom type pduMeanKWattsLCLTrapPer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 32000),
    )


_PduMeanKWattsLCLTrapPer_Type.__name__ = "Integer32"
_PduMeanKWattsLCLTrapPer_Object = MibTableColumn
pduMeanKWattsLCLTrapPer = _PduMeanKWattsLCLTrapPer_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 4, 1, 20),
    _PduMeanKWattsLCLTrapPer_Type()
)
pduMeanKWattsLCLTrapPer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduMeanKWattsLCLTrapPer.setStatus("current")


class _PduPwrFactorUCLTrapPer_Type(Integer32):
    """Custom type pduPwrFactorUCLTrapPer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 32000),
    )


_PduPwrFactorUCLTrapPer_Type.__name__ = "Integer32"
_PduPwrFactorUCLTrapPer_Object = MibTableColumn
pduPwrFactorUCLTrapPer = _PduPwrFactorUCLTrapPer_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 4, 1, 21),
    _PduPwrFactorUCLTrapPer_Type()
)
pduPwrFactorUCLTrapPer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduPwrFactorUCLTrapPer.setStatus("current")


class _PduPwrFactorUWLTrapPer_Type(Integer32):
    """Custom type pduPwrFactorUWLTrapPer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 32000),
    )


_PduPwrFactorUWLTrapPer_Type.__name__ = "Integer32"
_PduPwrFactorUWLTrapPer_Object = MibTableColumn
pduPwrFactorUWLTrapPer = _PduPwrFactorUWLTrapPer_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 4, 1, 22),
    _PduPwrFactorUWLTrapPer_Type()
)
pduPwrFactorUWLTrapPer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduPwrFactorUWLTrapPer.setStatus("current")


class _PduPwrFactorLWLTrapPer_Type(Integer32):
    """Custom type pduPwrFactorLWLTrapPer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 32000),
    )


_PduPwrFactorLWLTrapPer_Type.__name__ = "Integer32"
_PduPwrFactorLWLTrapPer_Object = MibTableColumn
pduPwrFactorLWLTrapPer = _PduPwrFactorLWLTrapPer_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 4, 1, 23),
    _PduPwrFactorLWLTrapPer_Type()
)
pduPwrFactorLWLTrapPer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduPwrFactorLWLTrapPer.setStatus("current")


class _PduPwrFactorLCLTrapPer_Type(Integer32):
    """Custom type pduPwrFactorLCLTrapPer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 32000),
    )


_PduPwrFactorLCLTrapPer_Type.__name__ = "Integer32"
_PduPwrFactorLCLTrapPer_Object = MibTableColumn
pduPwrFactorLCLTrapPer = _PduPwrFactorLCLTrapPer_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 7, 3, 4, 1, 24),
    _PduPwrFactorLCLTrapPer_Type()
)
pduPwrFactorLCLTrapPer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduPwrFactorLCLTrapPer.setStatus("current")
_Inventory_ObjectIdentity = ObjectIdentity
inventory = _Inventory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 99)
)


class _InvProdSignature_Type(DisplayString):
    """Custom type invProdSignature based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_InvProdSignature_Type.__name__ = "DisplayString"
_InvProdSignature_Object = MibScalar
invProdSignature = _InvProdSignature_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 99, 1),
    _InvProdSignature_Type()
)
invProdSignature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invProdSignature.setStatus("current")


class _InvProdFormatVer_Type(DisplayString):
    """Custom type invProdFormatVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_InvProdFormatVer_Type.__name__ = "DisplayString"
_InvProdFormatVer_Object = MibScalar
invProdFormatVer = _InvProdFormatVer_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 99, 2),
    _InvProdFormatVer_Type()
)
invProdFormatVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invProdFormatVer.setStatus("current")


class _InvManufCode_Type(DisplayString):
    """Custom type invManufCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_InvManufCode_Type.__name__ = "DisplayString"
_InvManufCode_Object = MibScalar
invManufCode = _InvManufCode_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 99, 3),
    _InvManufCode_Type()
)
invManufCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invManufCode.setStatus("current")


class _InvOrderNum_Type(DisplayString):
    """Custom type invOrderNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_InvOrderNum_Type.__name__ = "DisplayString"
_InvOrderNum_Object = MibScalar
invOrderNum = _InvOrderNum_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 99, 4),
    _InvOrderNum_Type()
)
invOrderNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invOrderNum.setStatus("current")


class _InvBatchNum_Type(DisplayString):
    """Custom type invBatchNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_InvBatchNum_Type.__name__ = "DisplayString"
_InvBatchNum_Object = MibScalar
invBatchNum = _InvBatchNum_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 99, 5),
    _InvBatchNum_Type()
)
invBatchNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invBatchNum.setStatus("current")


class _InvProdTestTime_Type(DisplayString):
    """Custom type invProdTestTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_InvProdTestTime_Type.__name__ = "DisplayString"
_InvProdTestTime_Object = MibScalar
invProdTestTime = _InvProdTestTime_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 99, 6),
    _InvProdTestTime_Type()
)
invProdTestTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invProdTestTime.setStatus("current")


class _InvUnitName_Type(DisplayString):
    """Custom type invUnitName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_InvUnitName_Type.__name__ = "DisplayString"
_InvUnitName_Object = MibScalar
invUnitName = _InvUnitName_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 99, 7),
    _InvUnitName_Type()
)
invUnitName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invUnitName.setStatus("current")


class _InvUnitPartNum_Type(DisplayString):
    """Custom type invUnitPartNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_InvUnitPartNum_Type.__name__ = "DisplayString"
_InvUnitPartNum_Object = MibScalar
invUnitPartNum = _InvUnitPartNum_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 99, 8),
    _InvUnitPartNum_Type()
)
invUnitPartNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invUnitPartNum.setStatus("current")


class _InvHwRevision_Type(DisplayString):
    """Custom type invHwRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_InvHwRevision_Type.__name__ = "DisplayString"
_InvHwRevision_Object = MibScalar
invHwRevision = _InvHwRevision_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 99, 9),
    _InvHwRevision_Type()
)
invHwRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invHwRevision.setStatus("current")


class _InvFwRevision_Type(DisplayString):
    """Custom type invFwRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_InvFwRevision_Type.__name__ = "DisplayString"
_InvFwRevision_Object = MibScalar
invFwRevision = _InvFwRevision_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 99, 10),
    _InvFwRevision_Type()
)
invFwRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invFwRevision.setStatus("current")


class _InvSerialNum_Type(DisplayString):
    """Custom type invSerialNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_InvSerialNum_Type.__name__ = "DisplayString"
_InvSerialNum_Object = MibScalar
invSerialNum = _InvSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 99, 11),
    _InvSerialNum_Type()
)
invSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invSerialNum.setStatus("current")
_InvDefaultIPAddrType_Type = InetAddressType
_InvDefaultIPAddrType_Object = MibScalar
invDefaultIPAddrType = _InvDefaultIPAddrType_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 99, 12),
    _InvDefaultIPAddrType_Type()
)
invDefaultIPAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invDefaultIPAddrType.setStatus("current")
_InvDefaultIPAddr_Type = InetAddress
_InvDefaultIPAddr_Object = MibScalar
invDefaultIPAddr = _InvDefaultIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 99, 13),
    _InvDefaultIPAddr_Type()
)
invDefaultIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invDefaultIPAddr.setStatus("current")
_InvDefaultSubNetMask_Type = InetAddress
_InvDefaultSubNetMask_Object = MibScalar
invDefaultSubNetMask = _InvDefaultSubNetMask_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 99, 14),
    _InvDefaultSubNetMask_Type()
)
invDefaultSubNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invDefaultSubNetMask.setStatus("current")
_InvDefaultGWAddr_Type = InetAddress
_InvDefaultGWAddr_Object = MibScalar
invDefaultGWAddr = _InvDefaultGWAddr_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 99, 15),
    _InvDefaultGWAddr_Type()
)
invDefaultGWAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invDefaultGWAddr.setStatus("current")
_InvMacAddr_Type = MacAddress
_InvMacAddr_Object = MibScalar
invMacAddr = _InvMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 99, 16),
    _InvMacAddr_Type()
)
invMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invMacAddr.setStatus("current")
_InvOk_Type = TruthValue
_InvOk_Object = MibScalar
invOk = _InvOk_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 99, 20),
    _InvOk_Type()
)
invOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invOk.setStatus("current")


class _InvInputCount_Type(Integer32):
    """Custom type invInputCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_InvInputCount_Type.__name__ = "Integer32"
_InvInputCount_Object = MibScalar
invInputCount = _InvInputCount_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 99, 50),
    _InvInputCount_Type()
)
invInputCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invInputCount.setStatus("current")


class _InvOutputCount_Type(Integer32):
    """Custom type invOutputCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_InvOutputCount_Type.__name__ = "Integer32"
_InvOutputCount_Object = MibScalar
invOutputCount = _InvOutputCount_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 99, 51),
    _InvOutputCount_Type()
)
invOutputCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invOutputCount.setStatus("current")


class _InvKeypadCount_Type(Integer32):
    """Custom type invKeypadCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_InvKeypadCount_Type.__name__ = "Integer32"
_InvKeypadCount_Object = MibScalar
invKeypadCount = _InvKeypadCount_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 99, 52),
    _InvKeypadCount_Type()
)
invKeypadCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invKeypadCount.setStatus("current")


class _InvAcuCount_Type(Integer32):
    """Custom type invAcuCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_InvAcuCount_Type.__name__ = "Integer32"
_InvAcuCount_Object = MibScalar
invAcuCount = _InvAcuCount_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 99, 53),
    _InvAcuCount_Type()
)
invAcuCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invAcuCount.setStatus("current")


class _InvAccessUserCount_Type(Integer32):
    """Custom type invAccessUserCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_InvAccessUserCount_Type.__name__ = "Integer32"
_InvAccessUserCount_Object = MibScalar
invAccessUserCount = _InvAccessUserCount_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 99, 54),
    _InvAccessUserCount_Type()
)
invAccessUserCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invAccessUserCount.setStatus("current")


class _InvPduCount_Type(Integer32):
    """Custom type invPduCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_InvPduCount_Type.__name__ = "Integer32"
_InvPduCount_Object = MibScalar
invPduCount = _InvPduCount_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 99, 55),
    _InvPduCount_Type()
)
invPduCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invPduCount.setStatus("current")
_TrapInfo_ObjectIdentity = ObjectIdentity
trapInfo = _TrapInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 100)
)
_TrapCode_Type = Unsigned32
_TrapCode_Object = MibScalar
trapCode = _TrapCode_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 100, 1),
    _TrapCode_Type()
)
trapCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapCode.setStatus("current")


class _TrapDescription_Type(DisplayString):
    """Custom type trapDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_TrapDescription_Type.__name__ = "DisplayString"
_TrapDescription_Object = MibScalar
trapDescription = _TrapDescription_Object(
    (1, 3, 6, 1, 4, 1, 3711, 24, 1, 1, 100, 2),
    _TrapDescription_Type()
)
trapDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapDescription.setStatus("current")

# Managed Objects groups


# Notification objects

alarmCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 3711, 24, 0, 1)
)
alarmCritical.setObjects(
      *(("HAWK-I2-MIB", "trapCode"),
        ("HAWK-I2-MIB", "trapDescription"))
)
if mibBuilder.loadTexts:
    alarmCritical.setStatus(
        "current"
    )

alarmWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 3711, 24, 0, 2)
)
alarmWarning.setObjects(
      *(("HAWK-I2-MIB", "trapCode"),
        ("HAWK-I2-MIB", "trapDescription"))
)
if mibBuilder.loadTexts:
    alarmWarning.setStatus(
        "current"
    )

alarmInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 3711, 24, 0, 3)
)
alarmInformation.setObjects(
      *(("HAWK-I2-MIB", "trapCode"),
        ("HAWK-I2-MIB", "trapDescription"))
)
if mibBuilder.loadTexts:
    alarmInformation.setStatus(
        "current"
    )

alarmCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 3711, 24, 0, 4)
)
alarmCleared.setObjects(
      *(("HAWK-I2-MIB", "trapCode"),
        ("HAWK-I2-MIB", "trapDescription"))
)
if mibBuilder.loadTexts:
    alarmCleared.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HAWK-I2-MIB",
    **{"DisplayString": DisplayString,
       "ContactState": ContactState,
       "InputContactState": InputContactState,
       "RelayState": RelayState,
       "OutputControlState": OutputControlState,
       "EnableState": EnableState,
       "InputDataType": InputDataType,
       "sinetica": sinetica,
       "hawki2MIB": hawki2MIB,
       "traps": traps,
       "alarmCritical": alarmCritical,
       "alarmWarning": alarmWarning,
       "alarmInformation": alarmInformation,
       "alarmCleared": alarmCleared,
       "v1": v1,
       "objects": objects,
       "inputs": inputs,
       "ipCommon": ipCommon,
       "ipEnable": ipEnable,
       "ipSelect": ipSelect,
       "ipInsert": ipInsert,
       "ipTHA": ipTHA,
       "ipTempScaleFlag": ipTempScaleFlag,
       "ipTHATable": ipTHATable,
       "ipTHAEntry": ipTHAEntry,
       "ipTHAChan": ipTHAChan,
       "ipTHARS": ipTHARS,
       "ipTHAName": ipTHAName,
       "ipTHALocn": ipTHALocn,
       "ipTHAAutoDetect": ipTHAAutoDetect,
       "ipTHAType": ipTHAType,
       "ipTHAValue": ipTHAValue,
       "ipTHAScaling": ipTHAScaling,
       "ipTHAOffset": ipTHAOffset,
       "ipTHAHysteresis": ipTHAHysteresis,
       "ipTHATrapsCfg": ipTHATrapsCfg,
       "ipTHAThreshTable": ipTHAThreshTable,
       "ipTHAThreshEntry": ipTHAThreshEntry,
       "ipTHAThreshChan": ipTHAThreshChan,
       "ipTHAThreshRS": ipTHAThreshRS,
       "ipTHAUCL": ipTHAUCL,
       "ipTHAUWL": ipTHAUWL,
       "ipTHALWL": ipTHALWL,
       "ipTHALCL": ipTHALCL,
       "ipTHATrapEnTable": ipTHATrapEnTable,
       "ipTHATrapEnEntry": ipTHATrapEnEntry,
       "ipTHATrapEnChan": ipTHATrapEnChan,
       "ipTHATrapEnRS": ipTHATrapEnRS,
       "ipTHAUCLTrapEn": ipTHAUCLTrapEn,
       "ipTHAUWLTrapEn": ipTHAUWLTrapEn,
       "ipTHALWLTrapEn": ipTHALWLTrapEn,
       "ipTHALCLTrapEn": ipTHALCLTrapEn,
       "ipTHATrapPerTable": ipTHATrapPerTable,
       "ipTHATrapPerEntry": ipTHATrapPerEntry,
       "ipTHATrapPerChan": ipTHATrapPerChan,
       "ipTHATrapPerRS": ipTHATrapPerRS,
       "ipTHATrapUCLPer": ipTHATrapUCLPer,
       "ipTHATrapUWLPer": ipTHATrapUWLPer,
       "ipTHATrapLWLPer": ipTHATrapLWLPer,
       "ipTHATrapLCLPer": ipTHATrapLCLPer,
       "ipContact": ipContact,
       "ipContTable": ipContTable,
       "ipContEntry": ipContEntry,
       "ipContChan": ipContChan,
       "ipContRS": ipContRS,
       "ipContName": ipContName,
       "ipContLocn": ipContLocn,
       "ipContAutoDetect": ipContAutoDetect,
       "ipContNormState": ipContNormState,
       "ipContCurrState": ipContCurrState,
       "ipContTrigMode": ipContTrigMode,
       "ipContReset": ipContReset,
       "ipContTrapEn": ipContTrapEn,
       "ipContTrapPeriod": ipContTrapPeriod,
       "outputs": outputs,
       "opEnable": opEnable,
       "opSelect": opSelect,
       "opInsert": opInsert,
       "opTable": opTable,
       "opEntry": opEntry,
       "opChan": opChan,
       "opRS": opRS,
       "opName": opName,
       "opLocn": opLocn,
       "opNormState": opNormState,
       "opCurrState": opCurrState,
       "opOnDelTime": opOnDelTime,
       "opOffDelTime": opOffDelTime,
       "opBooleanEqn": opBooleanEqn,
       "opTrapEn": opTrapEn,
       "opTrapPeriod": opTrapPeriod,
       "opControlState": opControlState,
       "keypads": keypads,
       "kpEnable": kpEnable,
       "kpSelect": kpSelect,
       "kpInsert": kpInsert,
       "kpCtlTable": kpCtlTable,
       "kpCtlEntry": kpCtlEntry,
       "kpNumber": kpNumber,
       "kpRS": kpRS,
       "kpManufacturer": kpManufacturer,
       "kpName": kpName,
       "kpDoorLatchTimeOut": kpDoorLatchTimeOut,
       "kpRtnToStndbyTimeOut": kpRtnToStndbyTimeOut,
       "kpEntryCodeValid": kpEntryCodeValid,
       "kpDoorOpenTimeOut": kpDoorOpenTimeOut,
       "kpRemoteDoorOpen": kpRemoteDoorOpen,
       "kpInUseTrapEn": kpInUseTrapEn,
       "acus": acus,
       "acuEnable": acuEnable,
       "acuSelect": acuSelect,
       "acuInsert": acuInsert,
       "acuCtlTable": acuCtlTable,
       "acuCtlEntry": acuCtlEntry,
       "acuNumber": acuNumber,
       "acuCtlRS": acuCtlRS,
       "acuManufacturer": acuManufacturer,
       "acuName": acuName,
       "acuDoorLatchTimeOut": acuDoorLatchTimeOut,
       "acuRtnToStndbyTimeOut": acuRtnToStndbyTimeOut,
       "acuEntryCodeValid": acuEntryCodeValid,
       "acuDoorOpenTimeOut": acuDoorOpenTimeOut,
       "acuRemoteDoorOpen": acuRemoteDoorOpen,
       "acuInUseTrapEn": acuInUseTrapEn,
       "access": access,
       "accUserCtl": accUserCtl,
       "accUserInstance": accUserInstance,
       "accUserTable": accUserTable,
       "accUserEntry": accUserEntry,
       "accUserNumber": accUserNumber,
       "accUserRS": accUserRS,
       "accUserName": accUserName,
       "accUserCode": accUserCode,
       "accUserPrivileges": accUserPrivileges,
       "accUserExpires": accUserExpires,
       "accUserSetup": accUserSetup,
       "pdus": pdus,
       "pduCommon": pduCommon,
       "pdusEnable": pdusEnable,
       "pduSelect": pduSelect,
       "pduInsert": pduInsert,
       "pduTable": pduTable,
       "pduEntry": pduEntry,
       "pduNumber": pduNumber,
       "pduRS": pduRS,
       "pduName": pduName,
       "pduOutEn": pduOutEn,
       "pduMonEn": pduMonEn,
       "pduCommsFail": pduCommsFail,
       "pduOutlets": pduOutlets,
       "pduOutAll": pduOutAll,
       "pduOutCycleAll": pduOutCycleAll,
       "pduOutCycleAllPwd": pduOutCycleAllPwd,
       "pduOutCycleAllAbort": pduOutCycleAllAbort,
       "pduOutGlobalCycleDelay": pduOutGlobalCycleDelay,
       "pduOutGlobalRebootTime": pduOutGlobalRebootTime,
       "pduOutGlobalCycleAbortTime": pduOutGlobalCycleAbortTime,
       "pduOutCmnTable": pduOutCmnTable,
       "pduOutCmnEntry": pduOutCmnEntry,
       "pduOutCmnPduNumber": pduOutCmnPduNumber,
       "pduOutCmnRS": pduOutCmnRS,
       "pduNumOfOutlets": pduNumOfOutlets,
       "pduOutCycle": pduOutCycle,
       "pduOutCyclePwd": pduOutCyclePwd,
       "pduOutCycleAbortTask": pduOutCycleAbortTask,
       "pduOutCycleAbortTime": pduOutCycleAbortTime,
       "pduOutTable": pduOutTable,
       "pduOutEntry": pduOutEntry,
       "pduOutPduNumber": pduOutPduNumber,
       "pduOutNumber": pduOutNumber,
       "pduOutRS": pduOutRS,
       "pduOutName": pduOutName,
       "pduOutOn": pduOutOn,
       "pduOutPwd": pduOutPwd,
       "pduOutCycleDelay": pduOutCycleDelay,
       "pduOutRebootPeriod": pduOutRebootPeriod,
       "pduMonitor": pduMonitor,
       "pduMonTable": pduMonTable,
       "pduMonEntry": pduMonEntry,
       "pduMonPduNumber": pduMonPduNumber,
       "pduMonRS": pduMonRS,
       "pduRMSVoltsValue": pduRMSVoltsValue,
       "pduRMSAmpsValue": pduRMSAmpsValue,
       "pduTotalEnergyValue": pduTotalEnergyValue,
       "pduMeanKVAValue": pduMeanKVAValue,
       "pduMeanKWattsValue": pduMeanKWattsValue,
       "pduPwrFactorValue": pduPwrFactorValue,
       "pduTrapThreshTable": pduTrapThreshTable,
       "pduTrapThreshEntry": pduTrapThreshEntry,
       "pduTrapThreshPduNumber": pduTrapThreshPduNumber,
       "pduTrapThreshRS": pduTrapThreshRS,
       "pduRMSVoltsUCL": pduRMSVoltsUCL,
       "pduRMSVoltsUWL": pduRMSVoltsUWL,
       "pduRMSVoltsLWL": pduRMSVoltsLWL,
       "pduRMSVoltsLCL": pduRMSVoltsLCL,
       "pduRMSAmpsUCL": pduRMSAmpsUCL,
       "pduRMSAmpsUWL": pduRMSAmpsUWL,
       "pduRMSAmpsLWL": pduRMSAmpsLWL,
       "pduRMSAmpsLCL": pduRMSAmpsLCL,
       "pduEnergyUCL": pduEnergyUCL,
       "pduEnergyUWL": pduEnergyUWL,
       "pduMeanKVAUCL": pduMeanKVAUCL,
       "pduMeanKVAUWL": pduMeanKVAUWL,
       "pduMeanKVALWL": pduMeanKVALWL,
       "pduMeanKVALCL": pduMeanKVALCL,
       "pduMeanKWattsUCL": pduMeanKWattsUCL,
       "pduMeanKWattsUWL": pduMeanKWattsUWL,
       "pduMeanKWattsLWL": pduMeanKWattsLWL,
       "pduMeanKWattsLCL": pduMeanKWattsLCL,
       "pduPwrFactorUCL": pduPwrFactorUCL,
       "pduPwrFactorUWL": pduPwrFactorUWL,
       "pduPwrFactorLWL": pduPwrFactorLWL,
       "pduPwrFactorLCL": pduPwrFactorLCL,
       "pduTrapEnTable": pduTrapEnTable,
       "pduTrapEnEntry": pduTrapEnEntry,
       "pduTrapEnPduNumber": pduTrapEnPduNumber,
       "pduTrapEnRS": pduTrapEnRS,
       "pduRMSVoltsUCLTrapEn": pduRMSVoltsUCLTrapEn,
       "pduRMSVoltsUWLTrapEn": pduRMSVoltsUWLTrapEn,
       "pduRMSVoltsLWLTrapEn": pduRMSVoltsLWLTrapEn,
       "pduRMSVoltsLCLTrapEn": pduRMSVoltsLCLTrapEn,
       "pduRMSAmpsUCLTrapEn": pduRMSAmpsUCLTrapEn,
       "pduRMSAmpsUWLTrapEn": pduRMSAmpsUWLTrapEn,
       "pduRMSAmpsLWLTrapEn": pduRMSAmpsLWLTrapEn,
       "pduRMSAmpsLCLTrapEn": pduRMSAmpsLCLTrapEn,
       "pduEnergyUCLTrapEn": pduEnergyUCLTrapEn,
       "pduEnergyUWLTrapEn": pduEnergyUWLTrapEn,
       "pduMeanKVAUCLTrapEn": pduMeanKVAUCLTrapEn,
       "pduMeanKVAUWLTrapEn": pduMeanKVAUWLTrapEn,
       "pduMeanKVALWLTrapEn": pduMeanKVALWLTrapEn,
       "pduMeanKVALCLTrapEn": pduMeanKVALCLTrapEn,
       "pduMeanKWattsUCLTrapEn": pduMeanKWattsUCLTrapEn,
       "pduMeanKWattsUWLTrapEn": pduMeanKWattsUWLTrapEn,
       "pduMeanKWattsLWLTrapEn": pduMeanKWattsLWLTrapEn,
       "pduMeanKWattsLCLTrapEn": pduMeanKWattsLCLTrapEn,
       "pduPwrFactorUCLTrapEn": pduPwrFactorUCLTrapEn,
       "pduPwrFactorUWLTrapEn": pduPwrFactorUWLTrapEn,
       "pduPwrFactorLWLTrapEn": pduPwrFactorLWLTrapEn,
       "pduPwrFactorLCLTrapEn": pduPwrFactorLCLTrapEn,
       "pduTrapPerTable": pduTrapPerTable,
       "pduTrapPerEntry": pduTrapPerEntry,
       "pduTrapPduNumber": pduTrapPduNumber,
       "pduTrapPerRS": pduTrapPerRS,
       "pduRMSVoltsUCLTrapPer": pduRMSVoltsUCLTrapPer,
       "pduRMSVoltsUWLTrapPer": pduRMSVoltsUWLTrapPer,
       "pduRMSVoltsLWLTrapPer": pduRMSVoltsLWLTrapPer,
       "pduRMSVoltsLCLTrapPer": pduRMSVoltsLCLTrapPer,
       "pduRMSAmpsUCLTrapPer": pduRMSAmpsUCLTrapPer,
       "pduRMSAmpsUWLTrapPer": pduRMSAmpsUWLTrapPer,
       "pduRMSAmpsLWLTrapPer": pduRMSAmpsLWLTrapPer,
       "pduRMSAmpsLCLTrapPer": pduRMSAmpsLCLTrapPer,
       "pduEnergyUCLTrapPer": pduEnergyUCLTrapPer,
       "pduEnergyUWLTrapPer": pduEnergyUWLTrapPer,
       "pduMeanKVAUCLTrapPer": pduMeanKVAUCLTrapPer,
       "pduMeanKVAUWLTrapPer": pduMeanKVAUWLTrapPer,
       "pduMeanKVALWLTrapPer": pduMeanKVALWLTrapPer,
       "pduMeanKVALCLTrapPer": pduMeanKVALCLTrapPer,
       "pduMeanKWattsUCLTrapPer": pduMeanKWattsUCLTrapPer,
       "pduMeanKWattsUWLTrapPer": pduMeanKWattsUWLTrapPer,
       "pduMeanKWattsLWLTrapPer": pduMeanKWattsLWLTrapPer,
       "pduMeanKWattsLCLTrapPer": pduMeanKWattsLCLTrapPer,
       "pduPwrFactorUCLTrapPer": pduPwrFactorUCLTrapPer,
       "pduPwrFactorUWLTrapPer": pduPwrFactorUWLTrapPer,
       "pduPwrFactorLWLTrapPer": pduPwrFactorLWLTrapPer,
       "pduPwrFactorLCLTrapPer": pduPwrFactorLCLTrapPer,
       "inventory": inventory,
       "invProdSignature": invProdSignature,
       "invProdFormatVer": invProdFormatVer,
       "invManufCode": invManufCode,
       "invOrderNum": invOrderNum,
       "invBatchNum": invBatchNum,
       "invProdTestTime": invProdTestTime,
       "invUnitName": invUnitName,
       "invUnitPartNum": invUnitPartNum,
       "invHwRevision": invHwRevision,
       "invFwRevision": invFwRevision,
       "invSerialNum": invSerialNum,
       "invDefaultIPAddrType": invDefaultIPAddrType,
       "invDefaultIPAddr": invDefaultIPAddr,
       "invDefaultSubNetMask": invDefaultSubNetMask,
       "invDefaultGWAddr": invDefaultGWAddr,
       "invMacAddr": invMacAddr,
       "invOk": invOk,
       "invInputCount": invInputCount,
       "invOutputCount": invOutputCount,
       "invKeypadCount": invKeypadCount,
       "invAcuCount": invAcuCount,
       "invAccessUserCount": invAccessUserCount,
       "invPduCount": invPduCount,
       "trapInfo": trapInfo,
       "trapCode": trapCode,
       "trapDescription": trapDescription}
)
