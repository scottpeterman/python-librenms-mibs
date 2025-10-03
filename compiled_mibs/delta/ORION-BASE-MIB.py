# SNMP MIB module (ORION-BASE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\delta\ORION-BASE-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:36:21 2025
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

(modules,
 orion) = mibBuilder.importSymbols(
    "GLOBAL-REG",
    "modules",
    "orion")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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

orionBaseMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 20246, 2, 1, 1, 2)
)
if mibBuilder.loadTexts:
    orionBaseMibModule.setRevisions(
        ("2012-04-27 12:00",
         "2012-01-26 14:15",
         "2011-06-20 07:34",
         "2011-02-10 09:01",
         "2010-06-16 10:27",
         "2010-02-24 10:46",
         "2009-09-04 09:52",
         "2008-02-21 14:39",
         "2008-01-18 08:35",
         "2006-07-27 10:26",
         "2006-03-02 08:55",
         "2006-02-23 09:32",
         "2005-06-03 11:07")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_OrionBaseMib_ObjectIdentity = ObjectIdentity
orionBaseMib = _OrionBaseMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1)
)
_ControllerConfs_ObjectIdentity = ObjectIdentity
controllerConfs = _ControllerConfs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 1)
)
_ControllerGroups_ObjectIdentity = ObjectIdentity
controllerGroups = _ControllerGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 1, 1)
)
_ControllerCompl_ObjectIdentity = ObjectIdentity
controllerCompl = _ControllerCompl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 1, 2)
)
_ControllerObjects_ObjectIdentity = ObjectIdentity
controllerObjects = _ControllerObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2)
)
_DcSystemInfo_ObjectIdentity = ObjectIdentity
dcSystemInfo = _DcSystemInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 1)
)


class _DcSiteName_Type(DisplayString):
    """Custom type dcSiteName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_DcSiteName_Type.__name__ = "DisplayString"
_DcSiteName_Object = MibScalar
dcSiteName = _DcSiteName_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 1, 1),
    _DcSiteName_Type()
)
dcSiteName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcSiteName.setStatus("current")


class _DcSystemName_Type(DisplayString):
    """Custom type dcSystemName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_DcSystemName_Type.__name__ = "DisplayString"
_DcSystemName_Object = MibScalar
dcSystemName = _DcSystemName_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 1, 2),
    _DcSystemName_Type()
)
dcSystemName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcSystemName.setStatus("current")


class _DcSystemDateTime_Type(DisplayString):
    """Custom type dcSystemDateTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(19, 19),
    )
    fixed_length = 19


_DcSystemDateTime_Type.__name__ = "DisplayString"
_DcSystemDateTime_Object = MibScalar
dcSystemDateTime = _DcSystemDateTime_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 1, 3),
    _DcSystemDateTime_Type()
)
dcSystemDateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcSystemDateTime.setStatus("current")


class _DcSoftwareVersion_Type(DisplayString):
    """Custom type dcSoftwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 12),
    )


_DcSoftwareVersion_Type.__name__ = "DisplayString"
_DcSoftwareVersion_Object = MibScalar
dcSoftwareVersion = _DcSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 1, 4),
    _DcSoftwareVersion_Type()
)
dcSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcSoftwareVersion.setStatus("current")
_DcSystemAlarms_ObjectIdentity = ObjectIdentity
dcSystemAlarms = _DcSystemAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 2)
)
_DcEventHistoryTable_Object = MibTable
dcEventHistoryTable = _DcEventHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    dcEventHistoryTable.setStatus("current")
_DcEventHistoryEntry_Object = MibTableRow
dcEventHistoryEntry = _DcEventHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 2, 1, 1)
)
dcEventHistoryEntry.setIndexNames(
    (0, "ORION-BASE-MIB", "dcEventHistoryIndex"),
)
if mibBuilder.loadTexts:
    dcEventHistoryEntry.setStatus("current")


class _DcEventHistoryIndex_Type(Integer32):
    """Custom type dcEventHistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_DcEventHistoryIndex_Type.__name__ = "Integer32"
_DcEventHistoryIndex_Object = MibTableColumn
dcEventHistoryIndex = _DcEventHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 2, 1, 1, 1),
    _DcEventHistoryIndex_Type()
)
dcEventHistoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dcEventHistoryIndex.setStatus("current")


class _DcEventHistoryTimestamp_Type(DisplayString):
    """Custom type dcEventHistoryTimestamp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(19, 19),
    )
    fixed_length = 19


_DcEventHistoryTimestamp_Type.__name__ = "DisplayString"
_DcEventHistoryTimestamp_Object = MibTableColumn
dcEventHistoryTimestamp = _DcEventHistoryTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 2, 1, 1, 2),
    _DcEventHistoryTimestamp_Type()
)
dcEventHistoryTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcEventHistoryTimestamp.setStatus("current")


class _DcEventHistoryMessage_Type(DisplayString):
    """Custom type dcEventHistoryMessage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_DcEventHistoryMessage_Type.__name__ = "DisplayString"
_DcEventHistoryMessage_Object = MibTableColumn
dcEventHistoryMessage = _DcEventHistoryMessage_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 2, 1, 1, 3),
    _DcEventHistoryMessage_Type()
)
dcEventHistoryMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcEventHistoryMessage.setStatus("current")
_DcAlarmTable_Object = MibTable
dcAlarmTable = _DcAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 2, 2)
)
if mibBuilder.loadTexts:
    dcAlarmTable.setStatus("current")
_DcAlarmEntry_Object = MibTableRow
dcAlarmEntry = _DcAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 2, 2, 1)
)
dcAlarmEntry.setIndexNames(
    (0, "ORION-BASE-MIB", "dcAlarmIndex"),
)
if mibBuilder.loadTexts:
    dcAlarmEntry.setStatus("current")


class _DcAlarmIndex_Type(Integer32):
    """Custom type dcAlarmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_DcAlarmIndex_Type.__name__ = "Integer32"
_DcAlarmIndex_Object = MibTableColumn
dcAlarmIndex = _DcAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 2, 2, 1, 1),
    _DcAlarmIndex_Type()
)
dcAlarmIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dcAlarmIndex.setStatus("current")


class _DcAlarmEventCategory_Type(Integer32):
    """Custom type dcAlarmEventCategory based on Integer32"""
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
        *(("unknown", 1),
          ("urgent", 2),
          ("nonUrgent", 3),
          ("critical", 4))
    )


_DcAlarmEventCategory_Type.__name__ = "Integer32"
_DcAlarmEventCategory_Object = MibTableColumn
dcAlarmEventCategory = _DcAlarmEventCategory_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 2, 2, 1, 2),
    _DcAlarmEventCategory_Type()
)
dcAlarmEventCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcAlarmEventCategory.setStatus("current")


class _DcAlarmEventName_Type(DisplayString):
    """Custom type dcAlarmEventName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 35),
    )


_DcAlarmEventName_Type.__name__ = "DisplayString"
_DcAlarmEventName_Object = MibTableColumn
dcAlarmEventName = _DcAlarmEventName_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 2, 2, 1, 3),
    _DcAlarmEventName_Type()
)
dcAlarmEventName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcAlarmEventName.setStatus("current")
_DcAlarmEventIdentifier_Type = Gauge32
_DcAlarmEventIdentifier_Object = MibTableColumn
dcAlarmEventIdentifier = _DcAlarmEventIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 2, 2, 1, 4),
    _DcAlarmEventIdentifier_Type()
)
dcAlarmEventIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcAlarmEventIdentifier.setStatus("current")


class _DcAlarmEventValue_Type(Integer32):
    """Custom type dcAlarmEventValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 3))
    )


_DcAlarmEventValue_Type.__name__ = "Integer32"
_DcAlarmEventValue_Object = MibTableColumn
dcAlarmEventValue = _DcAlarmEventValue_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 2, 2, 1, 5),
    _DcAlarmEventValue_Type()
)
dcAlarmEventValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcAlarmEventValue.setStatus("current")
_DcNumberUrgentAlarms_Type = Gauge32
_DcNumberUrgentAlarms_Object = MibScalar
dcNumberUrgentAlarms = _DcNumberUrgentAlarms_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 2, 3),
    _DcNumberUrgentAlarms_Type()
)
dcNumberUrgentAlarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcNumberUrgentAlarms.setStatus("current")
_DcNumberNonUrgentAlarms_Type = Gauge32
_DcNumberNonUrgentAlarms_Object = MibScalar
dcNumberNonUrgentAlarms = _DcNumberNonUrgentAlarms_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 2, 4),
    _DcNumberNonUrgentAlarms_Type()
)
dcNumberNonUrgentAlarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcNumberNonUrgentAlarms.setStatus("current")


class _DcMainsFailureAlarm_Type(Integer32):
    """Custom type dcMainsFailureAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 1),
          ("active", 2))
    )


_DcMainsFailureAlarm_Type.__name__ = "Integer32"
_DcMainsFailureAlarm_Object = MibScalar
dcMainsFailureAlarm = _DcMainsFailureAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 2, 5),
    _DcMainsFailureAlarm_Type()
)
dcMainsFailureAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcMainsFailureAlarm.setStatus("current")
_DcUrgentAlarmIdentifier_Type = Gauge32
_DcUrgentAlarmIdentifier_Object = MibScalar
dcUrgentAlarmIdentifier = _DcUrgentAlarmIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 2, 6),
    _DcUrgentAlarmIdentifier_Type()
)
dcUrgentAlarmIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcUrgentAlarmIdentifier.setStatus("current")


class _DcUrgentAlarmValue_Type(Integer32):
    """Custom type dcUrgentAlarmValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("indeterminate", 2),
          ("true", 3))
    )


_DcUrgentAlarmValue_Type.__name__ = "Integer32"
_DcUrgentAlarmValue_Object = MibScalar
dcUrgentAlarmValue = _DcUrgentAlarmValue_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 2, 7),
    _DcUrgentAlarmValue_Type()
)
dcUrgentAlarmValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcUrgentAlarmValue.setStatus("current")
_DcNonUrgentAlarmIdentifier_Type = Gauge32
_DcNonUrgentAlarmIdentifier_Object = MibScalar
dcNonUrgentAlarmIdentifier = _DcNonUrgentAlarmIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 2, 8),
    _DcNonUrgentAlarmIdentifier_Type()
)
dcNonUrgentAlarmIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcNonUrgentAlarmIdentifier.setStatus("current")


class _DcNonUrgentAlarmValue_Type(Integer32):
    """Custom type dcNonUrgentAlarmValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("indeterminate", 2),
          ("true", 3))
    )


_DcNonUrgentAlarmValue_Type.__name__ = "Integer32"
_DcNonUrgentAlarmValue_Object = MibScalar
dcNonUrgentAlarmValue = _DcNonUrgentAlarmValue_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 2, 9),
    _DcNonUrgentAlarmValue_Type()
)
dcNonUrgentAlarmValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcNonUrgentAlarmValue.setStatus("current")


class _DcUrgentAlarmName_Type(DisplayString):
    """Custom type dcUrgentAlarmName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 35),
    )


_DcUrgentAlarmName_Type.__name__ = "DisplayString"
_DcUrgentAlarmName_Object = MibScalar
dcUrgentAlarmName = _DcUrgentAlarmName_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 2, 10),
    _DcUrgentAlarmName_Type()
)
dcUrgentAlarmName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcUrgentAlarmName.setStatus("current")


class _DcNonUrgentAlarmName_Type(DisplayString):
    """Custom type dcNonUrgentAlarmName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 35),
    )


_DcNonUrgentAlarmName_Type.__name__ = "DisplayString"
_DcNonUrgentAlarmName_Object = MibScalar
dcNonUrgentAlarmName = _DcNonUrgentAlarmName_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 2, 11),
    _DcNonUrgentAlarmName_Type()
)
dcNonUrgentAlarmName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcNonUrgentAlarmName.setStatus("current")
_DcGenericAlarmTable_Object = MibTable
dcGenericAlarmTable = _DcGenericAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 2, 12)
)
if mibBuilder.loadTexts:
    dcGenericAlarmTable.setStatus("current")
_DcGenericAlarmEntry_Object = MibTableRow
dcGenericAlarmEntry = _DcGenericAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 2, 12, 1)
)
dcGenericAlarmEntry.setIndexNames(
    (0, "ORION-BASE-MIB", "dcGenericAlarmIndex"),
)
if mibBuilder.loadTexts:
    dcGenericAlarmEntry.setStatus("current")


class _DcGenericAlarmIndex_Type(Integer32):
    """Custom type dcGenericAlarmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_DcGenericAlarmIndex_Type.__name__ = "Integer32"
_DcGenericAlarmIndex_Object = MibTableColumn
dcGenericAlarmIndex = _DcGenericAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 2, 12, 1, 1),
    _DcGenericAlarmIndex_Type()
)
dcGenericAlarmIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dcGenericAlarmIndex.setStatus("current")


class _DcGenericAlarmEventName_Type(DisplayString):
    """Custom type dcGenericAlarmEventName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 35),
    )


_DcGenericAlarmEventName_Type.__name__ = "DisplayString"
_DcGenericAlarmEventName_Object = MibTableColumn
dcGenericAlarmEventName = _DcGenericAlarmEventName_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 2, 12, 1, 2),
    _DcGenericAlarmEventName_Type()
)
dcGenericAlarmEventName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcGenericAlarmEventName.setStatus("current")
_DcGenericAlarmEventIdentifier_Type = Gauge32
_DcGenericAlarmEventIdentifier_Object = MibTableColumn
dcGenericAlarmEventIdentifier = _DcGenericAlarmEventIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 2, 12, 1, 3),
    _DcGenericAlarmEventIdentifier_Type()
)
dcGenericAlarmEventIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcGenericAlarmEventIdentifier.setStatus("current")


class _DcGenericAlarmEventValue_Type(Integer32):
    """Custom type dcGenericAlarmEventValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_DcGenericAlarmEventValue_Type.__name__ = "Integer32"
_DcGenericAlarmEventValue_Object = MibTableColumn
dcGenericAlarmEventValue = _DcGenericAlarmEventValue_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 2, 12, 1, 4),
    _DcGenericAlarmEventValue_Type()
)
dcGenericAlarmEventValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcGenericAlarmEventValue.setStatus("current")
_DcNumberCriticalAlarms_Type = Gauge32
_DcNumberCriticalAlarms_Object = MibScalar
dcNumberCriticalAlarms = _DcNumberCriticalAlarms_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 2, 13),
    _DcNumberCriticalAlarms_Type()
)
dcNumberCriticalAlarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcNumberCriticalAlarms.setStatus("current")
_DcCriticalAlarmIdentifier_Type = Gauge32
_DcCriticalAlarmIdentifier_Object = MibScalar
dcCriticalAlarmIdentifier = _DcCriticalAlarmIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 2, 14),
    _DcCriticalAlarmIdentifier_Type()
)
dcCriticalAlarmIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcCriticalAlarmIdentifier.setStatus("current")


class _DcCriticalAlarmValue_Type(Integer32):
    """Custom type dcCriticalAlarmValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("indeterminate", 2),
          ("true", 3))
    )


_DcCriticalAlarmValue_Type.__name__ = "Integer32"
_DcCriticalAlarmValue_Object = MibScalar
dcCriticalAlarmValue = _DcCriticalAlarmValue_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 2, 15),
    _DcCriticalAlarmValue_Type()
)
dcCriticalAlarmValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcCriticalAlarmValue.setStatus("current")


class _DcCriticalAlarmName_Type(DisplayString):
    """Custom type dcCriticalAlarmName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 35),
    )


_DcCriticalAlarmName_Type.__name__ = "DisplayString"
_DcCriticalAlarmName_Object = MibScalar
dcCriticalAlarmName = _DcCriticalAlarmName_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 2, 16),
    _DcCriticalAlarmName_Type()
)
dcCriticalAlarmName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcCriticalAlarmName.setStatus("current")
_DcSystemMonitor_ObjectIdentity = ObjectIdentity
dcSystemMonitor = _DcSystemMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 3)
)
_DcSystemVoltage_Type = Integer32
_DcSystemVoltage_Object = MibScalar
dcSystemVoltage = _DcSystemVoltage_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 3, 1),
    _DcSystemVoltage_Type()
)
dcSystemVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcSystemVoltage.setStatus("current")
if mibBuilder.loadTexts:
    dcSystemVoltage.setUnits("10 mV")
_DcLoadCurrent_Type = Integer32
_DcLoadCurrent_Object = MibScalar
dcLoadCurrent = _DcLoadCurrent_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 3, 2),
    _DcLoadCurrent_Type()
)
dcLoadCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcLoadCurrent.setStatus("current")
if mibBuilder.loadTexts:
    dcLoadCurrent.setUnits("100 mA")
_DcBatteryCurrent_Type = Integer32
_DcBatteryCurrent_Object = MibScalar
dcBatteryCurrent = _DcBatteryCurrent_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 3, 3),
    _DcBatteryCurrent_Type()
)
dcBatteryCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcBatteryCurrent.setStatus("current")
if mibBuilder.loadTexts:
    dcBatteryCurrent.setUnits("100 mA")
_DcBatteryTemperature_Type = Integer32
_DcBatteryTemperature_Object = MibScalar
dcBatteryTemperature = _DcBatteryTemperature_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 3, 4),
    _DcBatteryTemperature_Type()
)
dcBatteryTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcBatteryTemperature.setStatus("current")
if mibBuilder.loadTexts:
    dcBatteryTemperature.setUnits("0.1 C")


class _DcChargeState_Type(Integer32):
    """Custom type dcChargeState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("float", 1),
          ("discharge", 2),
          ("equalize", 3),
          ("boost", 4),
          ("battTest", 5),
          ("recharge", 6),
          ("sepCharge", 7),
          ("evCtrlCharge", 8))
    )


_DcChargeState_Type.__name__ = "Integer32"
_DcChargeState_Object = MibScalar
dcChargeState = _DcChargeState_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 3, 5),
    _DcChargeState_Type()
)
dcChargeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcChargeState.setStatus("current")


class _DcCurrentLimit_Type(Integer32):
    """Custom type dcCurrentLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 1),
          ("active", 2))
    )


_DcCurrentLimit_Type.__name__ = "Integer32"
_DcCurrentLimit_Object = MibScalar
dcCurrentLimit = _DcCurrentLimit_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 3, 6),
    _DcCurrentLimit_Type()
)
dcCurrentLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcCurrentLimit.setStatus("current")
_DcRectifierCurrent_Type = Integer32
_DcRectifierCurrent_Object = MibScalar
dcRectifierCurrent = _DcRectifierCurrent_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 3, 7),
    _DcRectifierCurrent_Type()
)
dcRectifierCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcRectifierCurrent.setStatus("current")
if mibBuilder.loadTexts:
    dcRectifierCurrent.setUnits("100 mA")
_DcSystemPower_Type = Integer32
_DcSystemPower_Object = MibScalar
dcSystemPower = _DcSystemPower_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 3, 8),
    _DcSystemPower_Type()
)
dcSystemPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcSystemPower.setStatus("current")
if mibBuilder.loadTexts:
    dcSystemPower.setUnits("1 W")
_DcRectifier_ObjectIdentity = ObjectIdentity
dcRectifier = _DcRectifier_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 4)
)


class _DcNumberRectifiers_Type(Gauge32):
    """Custom type dcNumberRectifiers based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_DcNumberRectifiers_Type.__name__ = "Gauge32"
_DcNumberRectifiers_Object = MibScalar
dcNumberRectifiers = _DcNumberRectifiers_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 4, 1),
    _DcNumberRectifiers_Type()
)
dcNumberRectifiers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcNumberRectifiers.setStatus("current")


class _DcNumberRectifiersFailure_Type(Gauge32):
    """Custom type dcNumberRectifiersFailure based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_DcNumberRectifiersFailure_Type.__name__ = "Gauge32"
_DcNumberRectifiersFailure_Object = MibScalar
dcNumberRectifiersFailure = _DcNumberRectifiersFailure_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 4, 2),
    _DcNumberRectifiersFailure_Type()
)
dcNumberRectifiersFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcNumberRectifiersFailure.setStatus("current")


class _DcNumberRectifiersOkay_Type(Gauge32):
    """Custom type dcNumberRectifiersOkay based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_DcNumberRectifiersOkay_Type.__name__ = "Gauge32"
_DcNumberRectifiersOkay_Object = MibScalar
dcNumberRectifiersOkay = _DcNumberRectifiersOkay_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 4, 3),
    _DcNumberRectifiersOkay_Type()
)
dcNumberRectifiersOkay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcNumberRectifiersOkay.setStatus("current")
_DcRectifierTable_Object = MibTable
dcRectifierTable = _DcRectifierTable_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 4, 4)
)
if mibBuilder.loadTexts:
    dcRectifierTable.setStatus("current")
_DcRectifierEntry_Object = MibTableRow
dcRectifierEntry = _DcRectifierEntry_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 4, 4, 1)
)
dcRectifierEntry.setIndexNames(
    (0, "ORION-BASE-MIB", "dcRectifierIndex"),
)
if mibBuilder.loadTexts:
    dcRectifierEntry.setStatus("current")


class _DcRectifierIndex_Type(Integer32):
    """Custom type dcRectifierIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_DcRectifierIndex_Type.__name__ = "Integer32"
_DcRectifierIndex_Object = MibTableColumn
dcRectifierIndex = _DcRectifierIndex_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 4, 4, 1, 1),
    _DcRectifierIndex_Type()
)
dcRectifierIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dcRectifierIndex.setStatus("current")


class _DcRectifierIdentifier_Type(DisplayString):
    """Custom type dcRectifierIdentifier based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_DcRectifierIdentifier_Type.__name__ = "DisplayString"
_DcRectifierIdentifier_Object = MibTableColumn
dcRectifierIdentifier = _DcRectifierIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 4, 4, 1, 2),
    _DcRectifierIdentifier_Type()
)
dcRectifierIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcRectifierIdentifier.setStatus("current")


class _DcRectifierStatus_Type(Integer32):
    """Custom type dcRectifierStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("off", 2),
          ("on", 3))
    )


_DcRectifierStatus_Type.__name__ = "Integer32"
_DcRectifierStatus_Object = MibTableColumn
dcRectifierStatus = _DcRectifierStatus_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 4, 4, 1, 3),
    _DcRectifierStatus_Type()
)
dcRectifierStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcRectifierStatus.setStatus("current")
_DcRectifierGroupTable_Object = MibTable
dcRectifierGroupTable = _DcRectifierGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 4, 5)
)
if mibBuilder.loadTexts:
    dcRectifierGroupTable.setStatus("current")
_DcRectifierGroupEntry_Object = MibTableRow
dcRectifierGroupEntry = _DcRectifierGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 4, 5, 1)
)
dcRectifierGroupEntry.setIndexNames(
    (0, "ORION-BASE-MIB", "dcRectifierGroupIndex"),
)
if mibBuilder.loadTexts:
    dcRectifierGroupEntry.setStatus("current")


class _DcRectifierGroupIndex_Type(Integer32):
    """Custom type dcRectifierGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_DcRectifierGroupIndex_Type.__name__ = "Integer32"
_DcRectifierGroupIndex_Object = MibTableColumn
dcRectifierGroupIndex = _DcRectifierGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 4, 5, 1, 1),
    _DcRectifierGroupIndex_Type()
)
dcRectifierGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dcRectifierGroupIndex.setStatus("current")


class _DcRectifierGroupName_Type(DisplayString):
    """Custom type dcRectifierGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_DcRectifierGroupName_Type.__name__ = "DisplayString"
_DcRectifierGroupName_Object = MibTableColumn
dcRectifierGroupName = _DcRectifierGroupName_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 4, 5, 1, 2),
    _DcRectifierGroupName_Type()
)
dcRectifierGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcRectifierGroupName.setStatus("current")


class _DcRectifierGroupRectifierType_Type(Integer32):
    """Custom type dcRectifierGroupRectifierType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
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
              15,
              16,
              17,
              18,
              19,
              20,
              21)
        )
    )
    namedValues = NamedValues(
        *(("unknown48V", 1),
          ("fR48V2000W", 2),
          ("dPR1200B48", 3),
          ("dPR1500B48", 4),
          ("dPR600B48", 5),
          ("dPR7200B48", 6),
          ("fR48to60V2000W", 7),
          ("unknown24V", 8),
          ("unknown60V", 9),
          ("dPR600B60", 10),
          ("dPR3500B48", 11),
          ("dPR3500B24", 12),
          ("dPR300B48", 13),
          ("dPR1600B48", 14),
          ("dPR2700B48", 15),
          ("dPR2400B48", 16),
          ("dPR4000B48", 17),
          ("dPR2900B48", 18),
          ("dPR4000B48to60", 19),
          ("dPR850B48", 20),
          ("dPR2000B48", 21))
    )


_DcRectifierGroupRectifierType_Type.__name__ = "Integer32"
_DcRectifierGroupRectifierType_Object = MibTableColumn
dcRectifierGroupRectifierType = _DcRectifierGroupRectifierType_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 4, 5, 1, 3),
    _DcRectifierGroupRectifierType_Type()
)
dcRectifierGroupRectifierType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcRectifierGroupRectifierType.setStatus("current")
_DcRectifierGroupDefaultVoltage_Type = Integer32
_DcRectifierGroupDefaultVoltage_Object = MibTableColumn
dcRectifierGroupDefaultVoltage = _DcRectifierGroupDefaultVoltage_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 4, 5, 1, 4),
    _DcRectifierGroupDefaultVoltage_Type()
)
dcRectifierGroupDefaultVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcRectifierGroupDefaultVoltage.setStatus("current")
if mibBuilder.loadTexts:
    dcRectifierGroupDefaultVoltage.setUnits("10 mV")
_DcRectifierGroupDefaultCurrentLimit_Type = Integer32
_DcRectifierGroupDefaultCurrentLimit_Object = MibTableColumn
dcRectifierGroupDefaultCurrentLimit = _DcRectifierGroupDefaultCurrentLimit_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 4, 5, 1, 5),
    _DcRectifierGroupDefaultCurrentLimit_Type()
)
dcRectifierGroupDefaultCurrentLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcRectifierGroupDefaultCurrentLimit.setStatus("current")
if mibBuilder.loadTexts:
    dcRectifierGroupDefaultCurrentLimit.setUnits("100 mA")
_DcRectifierGroupDefaultPowerLimit_Type = Integer32
_DcRectifierGroupDefaultPowerLimit_Object = MibTableColumn
dcRectifierGroupDefaultPowerLimit = _DcRectifierGroupDefaultPowerLimit_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 4, 5, 1, 6),
    _DcRectifierGroupDefaultPowerLimit_Type()
)
dcRectifierGroupDefaultPowerLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcRectifierGroupDefaultPowerLimit.setStatus("current")
if mibBuilder.loadTexts:
    dcRectifierGroupDefaultPowerLimit.setUnits("1 W")
_DcRectifierGroupInputLowOff_Type = Integer32
_DcRectifierGroupInputLowOff_Object = MibTableColumn
dcRectifierGroupInputLowOff = _DcRectifierGroupInputLowOff_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 4, 5, 1, 7),
    _DcRectifierGroupInputLowOff_Type()
)
dcRectifierGroupInputLowOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcRectifierGroupInputLowOff.setStatus("current")
if mibBuilder.loadTexts:
    dcRectifierGroupInputLowOff.setUnits("10 mV")
_DcRectifierGroupInputLowOn_Type = Integer32
_DcRectifierGroupInputLowOn_Object = MibTableColumn
dcRectifierGroupInputLowOn = _DcRectifierGroupInputLowOn_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 4, 5, 1, 8),
    _DcRectifierGroupInputLowOn_Type()
)
dcRectifierGroupInputLowOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcRectifierGroupInputLowOn.setStatus("current")
if mibBuilder.loadTexts:
    dcRectifierGroupInputLowOn.setUnits("10 mV")
_DcRectifierGroupStartupVoltage_Type = Integer32
_DcRectifierGroupStartupVoltage_Object = MibTableColumn
dcRectifierGroupStartupVoltage = _DcRectifierGroupStartupVoltage_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 4, 5, 1, 9),
    _DcRectifierGroupStartupVoltage_Type()
)
dcRectifierGroupStartupVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcRectifierGroupStartupVoltage.setStatus("current")
if mibBuilder.loadTexts:
    dcRectifierGroupStartupVoltage.setUnits("10 mV")
_DcRectifierGroupStartupCurrentLimit_Type = Integer32
_DcRectifierGroupStartupCurrentLimit_Object = MibTableColumn
dcRectifierGroupStartupCurrentLimit = _DcRectifierGroupStartupCurrentLimit_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 4, 5, 1, 10),
    _DcRectifierGroupStartupCurrentLimit_Type()
)
dcRectifierGroupStartupCurrentLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcRectifierGroupStartupCurrentLimit.setStatus("current")
if mibBuilder.loadTexts:
    dcRectifierGroupStartupCurrentLimit.setUnits("100 mA")
_DcRectifierGroupStartupPowerLimit_Type = Integer32
_DcRectifierGroupStartupPowerLimit_Object = MibTableColumn
dcRectifierGroupStartupPowerLimit = _DcRectifierGroupStartupPowerLimit_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 4, 5, 1, 11),
    _DcRectifierGroupStartupPowerLimit_Type()
)
dcRectifierGroupStartupPowerLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcRectifierGroupStartupPowerLimit.setStatus("current")
if mibBuilder.loadTexts:
    dcRectifierGroupStartupPowerLimit.setUnits("1 W")
_DcRectifierGroupStartupTimeLimit_Type = Gauge32
_DcRectifierGroupStartupTimeLimit_Object = MibTableColumn
dcRectifierGroupStartupTimeLimit = _DcRectifierGroupStartupTimeLimit_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 4, 5, 1, 12),
    _DcRectifierGroupStartupTimeLimit_Type()
)
dcRectifierGroupStartupTimeLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcRectifierGroupStartupTimeLimit.setStatus("current")
if mibBuilder.loadTexts:
    dcRectifierGroupStartupTimeLimit.setUnits("10 ms")
_DcRectifierGroupPowerupDelay_Type = Gauge32
_DcRectifierGroupPowerupDelay_Object = MibTableColumn
dcRectifierGroupPowerupDelay = _DcRectifierGroupPowerupDelay_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 4, 5, 1, 13),
    _DcRectifierGroupPowerupDelay_Type()
)
dcRectifierGroupPowerupDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcRectifierGroupPowerupDelay.setStatus("current")
if mibBuilder.loadTexts:
    dcRectifierGroupPowerupDelay.setUnits("10 ms")
_DcRectifierGroupPowerupTime_Type = Gauge32
_DcRectifierGroupPowerupTime_Object = MibTableColumn
dcRectifierGroupPowerupTime = _DcRectifierGroupPowerupTime_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 4, 5, 1, 14),
    _DcRectifierGroupPowerupTime_Type()
)
dcRectifierGroupPowerupTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcRectifierGroupPowerupTime.setStatus("current")
if mibBuilder.loadTexts:
    dcRectifierGroupPowerupTime.setUnits("10 ms")
_DcRectifierGroupUmaxOff_Type = Integer32
_DcRectifierGroupUmaxOff_Object = MibTableColumn
dcRectifierGroupUmaxOff = _DcRectifierGroupUmaxOff_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 4, 5, 1, 15),
    _DcRectifierGroupUmaxOff_Type()
)
dcRectifierGroupUmaxOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcRectifierGroupUmaxOff.setStatus("current")
if mibBuilder.loadTexts:
    dcRectifierGroupUmaxOff.setUnits("10 mV")
_DcRectifierFunctions_ObjectIdentity = ObjectIdentity
dcRectifierFunctions = _DcRectifierFunctions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 4, 6)
)
_DcEfficiencyCycling_ObjectIdentity = ObjectIdentity
dcEfficiencyCycling = _DcEfficiencyCycling_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 4, 6, 1)
)


class _DcEfficiencyCyclingEnabled_Type(Integer32):
    """Custom type dcEfficiencyCyclingEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_DcEfficiencyCyclingEnabled_Type.__name__ = "Integer32"
_DcEfficiencyCyclingEnabled_Object = MibScalar
dcEfficiencyCyclingEnabled = _DcEfficiencyCyclingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 4, 6, 1, 1),
    _DcEfficiencyCyclingEnabled_Type()
)
dcEfficiencyCyclingEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcEfficiencyCyclingEnabled.setStatus("current")


class _DcLimitSwitchingTimes_Type(Integer32):
    """Custom type dcLimitSwitchingTimes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_DcLimitSwitchingTimes_Type.__name__ = "Integer32"
_DcLimitSwitchingTimes_Object = MibScalar
dcLimitSwitchingTimes = _DcLimitSwitchingTimes_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 4, 6, 1, 2),
    _DcLimitSwitchingTimes_Type()
)
dcLimitSwitchingTimes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcLimitSwitchingTimes.setStatus("current")


class _DcForceSwitchingOncePerMonth_Type(Integer32):
    """Custom type dcForceSwitchingOncePerMonth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_DcForceSwitchingOncePerMonth_Type.__name__ = "Integer32"
_DcForceSwitchingOncePerMonth_Object = MibScalar
dcForceSwitchingOncePerMonth = _DcForceSwitchingOncePerMonth_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 4, 6, 1, 3),
    _DcForceSwitchingOncePerMonth_Type()
)
dcForceSwitchingOncePerMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcForceSwitchingOncePerMonth.setStatus("current")
_DcMaximumLoadStep_Type = Integer32
_DcMaximumLoadStep_Object = MibScalar
dcMaximumLoadStep = _DcMaximumLoadStep_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 4, 6, 1, 4),
    _DcMaximumLoadStep_Type()
)
dcMaximumLoadStep.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcMaximumLoadStep.setStatus("current")
if mibBuilder.loadTexts:
    dcMaximumLoadStep.setUnits("1 W")
_DcMinimumLoadStep_Type = Integer32
_DcMinimumLoadStep_Object = MibScalar
dcMinimumLoadStep = _DcMinimumLoadStep_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 4, 6, 1, 5),
    _DcMinimumLoadStep_Type()
)
dcMinimumLoadStep.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcMinimumLoadStep.setStatus("current")
if mibBuilder.loadTexts:
    dcMinimumLoadStep.setUnits("1 W")
_DcPowerLimitation_ObjectIdentity = ObjectIdentity
dcPowerLimitation = _DcPowerLimitation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 4, 6, 2)
)
_DcPowerLimitationTable_Object = MibTable
dcPowerLimitationTable = _DcPowerLimitationTable_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 4, 6, 2, 1)
)
if mibBuilder.loadTexts:
    dcPowerLimitationTable.setStatus("current")
_DcPowerLimitationEntry_Object = MibTableRow
dcPowerLimitationEntry = _DcPowerLimitationEntry_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 4, 6, 2, 1, 1)
)
dcPowerLimitationEntry.setIndexNames(
    (0, "ORION-BASE-MIB", "dcPowerLimitationIndex"),
)
if mibBuilder.loadTexts:
    dcPowerLimitationEntry.setStatus("current")


class _DcPowerLimitationIndex_Type(Integer32):
    """Custom type dcPowerLimitationIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_DcPowerLimitationIndex_Type.__name__ = "Integer32"
_DcPowerLimitationIndex_Object = MibTableColumn
dcPowerLimitationIndex = _DcPowerLimitationIndex_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 4, 6, 2, 1, 1, 1),
    _DcPowerLimitationIndex_Type()
)
dcPowerLimitationIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dcPowerLimitationIndex.setStatus("current")


class _DcPowerLimitationEventName_Type(DisplayString):
    """Custom type dcPowerLimitationEventName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 35),
    )


_DcPowerLimitationEventName_Type.__name__ = "DisplayString"
_DcPowerLimitationEventName_Object = MibTableColumn
dcPowerLimitationEventName = _DcPowerLimitationEventName_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 4, 6, 2, 1, 1, 2),
    _DcPowerLimitationEventName_Type()
)
dcPowerLimitationEventName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPowerLimitationEventName.setStatus("current")


class _DcPowerLimitationStatus_Type(Integer32):
    """Custom type dcPowerLimitationStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("inactive", 2),
          ("powerLimit", 3))
    )


_DcPowerLimitationStatus_Type.__name__ = "Integer32"
_DcPowerLimitationStatus_Object = MibTableColumn
dcPowerLimitationStatus = _DcPowerLimitationStatus_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 4, 6, 2, 1, 1, 3),
    _DcPowerLimitationStatus_Type()
)
dcPowerLimitationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPowerLimitationStatus.setStatus("current")


class _DcPowerLimitationType_Type(Integer32):
    """Custom type dcPowerLimitationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 1),
          ("fixedLimit", 2))
    )


_DcPowerLimitationType_Type.__name__ = "Integer32"
_DcPowerLimitationType_Object = MibTableColumn
dcPowerLimitationType = _DcPowerLimitationType_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 4, 6, 2, 1, 1, 4),
    _DcPowerLimitationType_Type()
)
dcPowerLimitationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPowerLimitationType.setStatus("current")
_DcPowerLimitationLimit_Type = Integer32
_DcPowerLimitationLimit_Object = MibTableColumn
dcPowerLimitationLimit = _DcPowerLimitationLimit_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 4, 6, 2, 1, 1, 5),
    _DcPowerLimitationLimit_Type()
)
dcPowerLimitationLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcPowerLimitationLimit.setStatus("current")
if mibBuilder.loadTexts:
    dcPowerLimitationLimit.setUnits("1 W")


class _DcPowerLimitationNoBatteryDischarge_Type(Integer32):
    """Custom type dcPowerLimitationNoBatteryDischarge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_DcPowerLimitationNoBatteryDischarge_Type.__name__ = "Integer32"
_DcPowerLimitationNoBatteryDischarge_Object = MibTableColumn
dcPowerLimitationNoBatteryDischarge = _DcPowerLimitationNoBatteryDischarge_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 4, 6, 2, 1, 1, 6),
    _DcPowerLimitationNoBatteryDischarge_Type()
)
dcPowerLimitationNoBatteryDischarge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcPowerLimitationNoBatteryDischarge.setStatus("current")
_DcBattery_ObjectIdentity = ObjectIdentity
dcBattery = _DcBattery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5)
)
_DcFloatCharge_ObjectIdentity = ObjectIdentity
dcFloatCharge = _DcFloatCharge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 1)
)
_DcUsys20_Type = Integer32
_DcUsys20_Object = MibScalar
dcUsys20 = _DcUsys20_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 1, 1),
    _DcUsys20_Type()
)
dcUsys20.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcUsys20.setStatus("current")
if mibBuilder.loadTexts:
    dcUsys20.setUnits("10 mV")
_DcBatteryTest_ObjectIdentity = ObjectIdentity
dcBatteryTest = _DcBatteryTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 2)
)
_DcBatteryTestParameter_ObjectIdentity = ObjectIdentity
dcBatteryTestParameter = _DcBatteryTestParameter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 2, 1)
)
_DcBatteryTestUsupport_Type = Integer32
_DcBatteryTestUsupport_Object = MibScalar
dcBatteryTestUsupport = _DcBatteryTestUsupport_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 2, 1, 1),
    _DcBatteryTestUsupport_Type()
)
dcBatteryTestUsupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcBatteryTestUsupport.setStatus("current")
if mibBuilder.loadTexts:
    dcBatteryTestUsupport.setUnits("10 mV")
_DcBatteryTestDuration_Type = Gauge32
_DcBatteryTestDuration_Object = MibScalar
dcBatteryTestDuration = _DcBatteryTestDuration_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 2, 1, 2),
    _DcBatteryTestDuration_Type()
)
dcBatteryTestDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcBatteryTestDuration.setStatus("current")
if mibBuilder.loadTexts:
    dcBatteryTestDuration.setUnits("minute")
_DcBatteryTestInterval_Type = Gauge32
_DcBatteryTestInterval_Object = MibScalar
dcBatteryTestInterval = _DcBatteryTestInterval_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 2, 1, 3),
    _DcBatteryTestInterval_Type()
)
dcBatteryTestInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcBatteryTestInterval.setStatus("current")
if mibBuilder.loadTexts:
    dcBatteryTestInterval.setUnits("days")
_DcBatteryTestDischargeCurrent_Type = Integer32
_DcBatteryTestDischargeCurrent_Object = MibScalar
dcBatteryTestDischargeCurrent = _DcBatteryTestDischargeCurrent_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 2, 1, 4),
    _DcBatteryTestDischargeCurrent_Type()
)
dcBatteryTestDischargeCurrent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcBatteryTestDischargeCurrent.setStatus("current")
if mibBuilder.loadTexts:
    dcBatteryTestDischargeCurrent.setUnits("100 mA")
_DcBatteryTestMinDuration_Type = Gauge32
_DcBatteryTestMinDuration_Object = MibScalar
dcBatteryTestMinDuration = _DcBatteryTestMinDuration_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 2, 1, 5),
    _DcBatteryTestMinDuration_Type()
)
dcBatteryTestMinDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcBatteryTestMinDuration.setStatus("current")
if mibBuilder.loadTexts:
    dcBatteryTestMinDuration.setUnits("minutes")
_DcBatteryTestVoltageWithinUfloat_Type = Integer32
_DcBatteryTestVoltageWithinUfloat_Object = MibScalar
dcBatteryTestVoltageWithinUfloat = _DcBatteryTestVoltageWithinUfloat_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 2, 1, 6),
    _DcBatteryTestVoltageWithinUfloat_Type()
)
dcBatteryTestVoltageWithinUfloat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcBatteryTestVoltageWithinUfloat.setStatus("current")
if mibBuilder.loadTexts:
    dcBatteryTestVoltageWithinUfloat.setUnits("10 mV")
_DcBatteryTestVoltageWithinUfloatPeriod_Type = Gauge32
_DcBatteryTestVoltageWithinUfloatPeriod_Object = MibScalar
dcBatteryTestVoltageWithinUfloatPeriod = _DcBatteryTestVoltageWithinUfloatPeriod_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 2, 1, 7),
    _DcBatteryTestVoltageWithinUfloatPeriod_Type()
)
dcBatteryTestVoltageWithinUfloatPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcBatteryTestVoltageWithinUfloatPeriod.setStatus("current")
if mibBuilder.loadTexts:
    dcBatteryTestVoltageWithinUfloatPeriod.setUnits("days")
_DcBatteryTestTempFrom_Type = Integer32
_DcBatteryTestTempFrom_Object = MibScalar
dcBatteryTestTempFrom = _DcBatteryTestTempFrom_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 2, 1, 8),
    _DcBatteryTestTempFrom_Type()
)
dcBatteryTestTempFrom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcBatteryTestTempFrom.setStatus("current")
if mibBuilder.loadTexts:
    dcBatteryTestTempFrom.setUnits("0.1 C")
_DcBatteryTestTempTo_Type = Integer32
_DcBatteryTestTempTo_Object = MibScalar
dcBatteryTestTempTo = _DcBatteryTestTempTo_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 2, 1, 9),
    _DcBatteryTestTempTo_Type()
)
dcBatteryTestTempTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcBatteryTestTempTo.setStatus("current")
if mibBuilder.loadTexts:
    dcBatteryTestTempTo.setUnits("0.1 C")


class _DcBatteryTestIntervalEnabled_Type(Integer32):
    """Custom type dcBatteryTestIntervalEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_DcBatteryTestIntervalEnabled_Type.__name__ = "Integer32"
_DcBatteryTestIntervalEnabled_Object = MibScalar
dcBatteryTestIntervalEnabled = _DcBatteryTestIntervalEnabled_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 2, 1, 10),
    _DcBatteryTestIntervalEnabled_Type()
)
dcBatteryTestIntervalEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcBatteryTestIntervalEnabled.setStatus("current")


class _DcBatteryTestStartTimeFrom_Type(DisplayString):
    """Custom type dcBatteryTestStartTimeFrom based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_DcBatteryTestStartTimeFrom_Type.__name__ = "DisplayString"
_DcBatteryTestStartTimeFrom_Object = MibScalar
dcBatteryTestStartTimeFrom = _DcBatteryTestStartTimeFrom_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 2, 1, 11),
    _DcBatteryTestStartTimeFrom_Type()
)
dcBatteryTestStartTimeFrom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcBatteryTestStartTimeFrom.setStatus("current")


class _DcBatteryTestStartTimeTo_Type(DisplayString):
    """Custom type dcBatteryTestStartTimeTo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_DcBatteryTestStartTimeTo_Type.__name__ = "DisplayString"
_DcBatteryTestStartTimeTo_Object = MibScalar
dcBatteryTestStartTimeTo = _DcBatteryTestStartTimeTo_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 2, 1, 12),
    _DcBatteryTestStartTimeTo_Type()
)
dcBatteryTestStartTimeTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcBatteryTestStartTimeTo.setStatus("current")
_DcBatteryTestResults_ObjectIdentity = ObjectIdentity
dcBatteryTestResults = _DcBatteryTestResults_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 2, 2)
)


class _DcBatteryTestDateTime_Type(DisplayString):
    """Custom type dcBatteryTestDateTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(19, 19),
    )
    fixed_length = 19


_DcBatteryTestDateTime_Type.__name__ = "DisplayString"
_DcBatteryTestDateTime_Object = MibScalar
dcBatteryTestDateTime = _DcBatteryTestDateTime_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 2, 2, 1),
    _DcBatteryTestDateTime_Type()
)
dcBatteryTestDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcBatteryTestDateTime.setStatus("current")


class _DcBatteryTestResult_Type(Integer32):
    """Custom type dcBatteryTestResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("failed", 2),
          ("aborted", 3),
          ("loadFailure", 4),
          ("okay", 5),
          ("abortedManual", 6),
          ("abortedEvCtrlCharge", 7),
          ("abortedInhibitEv", 8))
    )


_DcBatteryTestResult_Type.__name__ = "Integer32"
_DcBatteryTestResult_Object = MibScalar
dcBatteryTestResult = _DcBatteryTestResult_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 2, 2, 2),
    _DcBatteryTestResult_Type()
)
dcBatteryTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcBatteryTestResult.setStatus("current")
_DcBatteryTestEndVoltage_Type = Integer32
_DcBatteryTestEndVoltage_Object = MibScalar
dcBatteryTestEndVoltage = _DcBatteryTestEndVoltage_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 2, 2, 3),
    _DcBatteryTestEndVoltage_Type()
)
dcBatteryTestEndVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcBatteryTestEndVoltage.setStatus("current")
if mibBuilder.loadTexts:
    dcBatteryTestEndVoltage.setUnits("10 mV")


class _DcBatteryTestControl_Type(Integer32):
    """Custom type dcBatteryTestControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("start", 1),
          ("stop", 2))
    )


_DcBatteryTestControl_Type.__name__ = "Integer32"
_DcBatteryTestControl_Object = MibScalar
dcBatteryTestControl = _DcBatteryTestControl_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 2, 3),
    _DcBatteryTestControl_Type()
)
dcBatteryTestControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcBatteryTestControl.setStatus("current")


class _DcBatteryTestStatus_Type(Integer32):
    """Custom type dcBatteryTestStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 1),
          ("starting", 2),
          ("stopping", 3),
          ("constantCurrent", 4),
          ("timeBased", 5),
          ("energyBased", 6),
          ("recovery", 7),
          ("realLoad", 8),
          ("stop", 9))
    )


_DcBatteryTestStatus_Type.__name__ = "Integer32"
_DcBatteryTestStatus_Object = MibScalar
dcBatteryTestStatus = _DcBatteryTestStatus_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 2, 4),
    _DcBatteryTestStatus_Type()
)
dcBatteryTestStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcBatteryTestStatus.setStatus("current")


class _DcBatteryTestFailureEvent_Type(Integer32):
    """Custom type dcBatteryTestFailureEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_DcBatteryTestFailureEvent_Type.__name__ = "Integer32"
_DcBatteryTestFailureEvent_Object = MibScalar
dcBatteryTestFailureEvent = _DcBatteryTestFailureEvent_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 2, 5),
    _DcBatteryTestFailureEvent_Type()
)
dcBatteryTestFailureEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcBatteryTestFailureEvent.setStatus("current")


class _DcBatteryTestType_Type(Integer32):
    """Custom type dcBatteryTestType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              5)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("constantCurrent", 2),
          ("realLoad", 5))
    )


_DcBatteryTestType_Type.__name__ = "Integer32"
_DcBatteryTestType_Object = MibScalar
dcBatteryTestType = _DcBatteryTestType_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 2, 6),
    _DcBatteryTestType_Type()
)
dcBatteryTestType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcBatteryTestType.setStatus("current")
_DcBatteryParameter_ObjectIdentity = ObjectIdentity
dcBatteryParameter = _DcBatteryParameter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 3)
)
_DcTotalBatteryCapacity_Type = Gauge32
_DcTotalBatteryCapacity_Object = MibScalar
dcTotalBatteryCapacity = _DcTotalBatteryCapacity_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 3, 1),
    _DcTotalBatteryCapacity_Type()
)
dcTotalBatteryCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcTotalBatteryCapacity.setStatus("current")
if mibBuilder.loadTexts:
    dcTotalBatteryCapacity.setUnits("100 mAh")
_DcBatteryStringTable_Object = MibTable
dcBatteryStringTable = _DcBatteryStringTable_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 3, 2)
)
if mibBuilder.loadTexts:
    dcBatteryStringTable.setStatus("current")
_DcBatteryStringEntry_Object = MibTableRow
dcBatteryStringEntry = _DcBatteryStringEntry_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 3, 2, 1)
)
dcBatteryStringEntry.setIndexNames(
    (0, "ORION-BASE-MIB", "dcBatteryStringIndex"),
)
if mibBuilder.loadTexts:
    dcBatteryStringEntry.setStatus("current")


class _DcBatteryStringIndex_Type(Integer32):
    """Custom type dcBatteryStringIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_DcBatteryStringIndex_Type.__name__ = "Integer32"
_DcBatteryStringIndex_Object = MibTableColumn
dcBatteryStringIndex = _DcBatteryStringIndex_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 3, 2, 1, 1),
    _DcBatteryStringIndex_Type()
)
dcBatteryStringIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dcBatteryStringIndex.setStatus("current")


class _DcBatteryStringName_Type(DisplayString):
    """Custom type dcBatteryStringName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_DcBatteryStringName_Type.__name__ = "DisplayString"
_DcBatteryStringName_Object = MibTableColumn
dcBatteryStringName = _DcBatteryStringName_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 3, 2, 1, 2),
    _DcBatteryStringName_Type()
)
dcBatteryStringName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcBatteryStringName.setStatus("current")
_DcBatteryStringMaxIBatt_Type = Integer32
_DcBatteryStringMaxIBatt_Object = MibTableColumn
dcBatteryStringMaxIBatt = _DcBatteryStringMaxIBatt_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 3, 2, 1, 3),
    _DcBatteryStringMaxIBatt_Type()
)
dcBatteryStringMaxIBatt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcBatteryStringMaxIBatt.setStatus("current")
if mibBuilder.loadTexts:
    dcBatteryStringMaxIBatt.setUnits("100 mA")
_DcBatteryStringCapacity_Type = Gauge32
_DcBatteryStringCapacity_Object = MibTableColumn
dcBatteryStringCapacity = _DcBatteryStringCapacity_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 3, 2, 1, 4),
    _DcBatteryStringCapacity_Type()
)
dcBatteryStringCapacity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcBatteryStringCapacity.setStatus("current")
if mibBuilder.loadTexts:
    dcBatteryStringCapacity.setUnits("100 mAh")
_DcLossOfBackupTime_ObjectIdentity = ObjectIdentity
dcLossOfBackupTime = _DcLossOfBackupTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 3, 3)
)


class _DcLossOfBackupTimeEnabled_Type(Integer32):
    """Custom type dcLossOfBackupTimeEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_DcLossOfBackupTimeEnabled_Type.__name__ = "Integer32"
_DcLossOfBackupTimeEnabled_Object = MibScalar
dcLossOfBackupTimeEnabled = _DcLossOfBackupTimeEnabled_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 3, 3, 1),
    _DcLossOfBackupTimeEnabled_Type()
)
dcLossOfBackupTimeEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcLossOfBackupTimeEnabled.setStatus("current")


class _DcLossOfBackupTimeStatus_Type(Integer32):
    """Custom type dcLossOfBackupTimeStatus based on Integer32"""
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
        *(("inactive", 1),
          ("ok", 2),
          ("occured", 3),
          ("fail", 4))
    )


_DcLossOfBackupTimeStatus_Type.__name__ = "Integer32"
_DcLossOfBackupTimeStatus_Object = MibScalar
dcLossOfBackupTimeStatus = _DcLossOfBackupTimeStatus_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 3, 3, 2),
    _DcLossOfBackupTimeStatus_Type()
)
dcLossOfBackupTimeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcLossOfBackupTimeStatus.setStatus("current")
_DcExpectedBackupTime_Type = Gauge32
_DcExpectedBackupTime_Object = MibScalar
dcExpectedBackupTime = _DcExpectedBackupTime_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 3, 3, 3),
    _DcExpectedBackupTime_Type()
)
dcExpectedBackupTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcExpectedBackupTime.setStatus("current")
if mibBuilder.loadTexts:
    dcExpectedBackupTime.setUnits("minutes")
_DcEqualize_ObjectIdentity = ObjectIdentity
dcEqualize = _DcEqualize_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 4)
)


class _DcEqualizeControl_Type(Integer32):
    """Custom type dcEqualizeControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("start", 1),
          ("stop", 2))
    )


_DcEqualizeControl_Type.__name__ = "Integer32"
_DcEqualizeControl_Object = MibScalar
dcEqualizeControl = _DcEqualizeControl_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 4, 1),
    _DcEqualizeControl_Type()
)
dcEqualizeControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcEqualizeControl.setStatus("current")


class _DcEqualizeStatus_Type(Integer32):
    """Custom type dcEqualizeStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 1),
          ("starting", 2),
          ("stopping", 3),
          ("preparing", 4),
          ("cooking", 5),
          ("recovering", 6))
    )


_DcEqualizeStatus_Type.__name__ = "Integer32"
_DcEqualizeStatus_Object = MibScalar
dcEqualizeStatus = _DcEqualizeStatus_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 4, 2),
    _DcEqualizeStatus_Type()
)
dcEqualizeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcEqualizeStatus.setStatus("current")


class _DcEqualizeEnabled_Type(Integer32):
    """Custom type dcEqualizeEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_DcEqualizeEnabled_Type.__name__ = "Integer32"
_DcEqualizeEnabled_Object = MibScalar
dcEqualizeEnabled = _DcEqualizeEnabled_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 4, 3),
    _DcEqualizeEnabled_Type()
)
dcEqualizeEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcEqualizeEnabled.setStatus("current")
_DcEqualizeParameter_ObjectIdentity = ObjectIdentity
dcEqualizeParameter = _DcEqualizeParameter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 4, 4)
)
_DcEqualizeVoltage_Type = Integer32
_DcEqualizeVoltage_Object = MibScalar
dcEqualizeVoltage = _DcEqualizeVoltage_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 4, 4, 1),
    _DcEqualizeVoltage_Type()
)
dcEqualizeVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcEqualizeVoltage.setStatus("current")
if mibBuilder.loadTexts:
    dcEqualizeVoltage.setUnits("10 mV")
_DcEqualizeDuration_Type = Gauge32
_DcEqualizeDuration_Object = MibScalar
dcEqualizeDuration = _DcEqualizeDuration_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 4, 4, 2),
    _DcEqualizeDuration_Type()
)
dcEqualizeDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcEqualizeDuration.setStatus("current")
if mibBuilder.loadTexts:
    dcEqualizeDuration.setUnits("minutes")


class _DcEqualizeUseBattRoomFanEnabled_Type(Integer32):
    """Custom type dcEqualizeUseBattRoomFanEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_DcEqualizeUseBattRoomFanEnabled_Type.__name__ = "Integer32"
_DcEqualizeUseBattRoomFanEnabled_Object = MibScalar
dcEqualizeUseBattRoomFanEnabled = _DcEqualizeUseBattRoomFanEnabled_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 4, 4, 3),
    _DcEqualizeUseBattRoomFanEnabled_Type()
)
dcEqualizeUseBattRoomFanEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcEqualizeUseBattRoomFanEnabled.setStatus("current")
_DcEqualizeLeadTime_Type = Gauge32
_DcEqualizeLeadTime_Object = MibScalar
dcEqualizeLeadTime = _DcEqualizeLeadTime_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 4, 4, 4),
    _DcEqualizeLeadTime_Type()
)
dcEqualizeLeadTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcEqualizeLeadTime.setStatus("current")
if mibBuilder.loadTexts:
    dcEqualizeLeadTime.setUnits("minutes")
_DcEqualizeTimeLag_Type = Gauge32
_DcEqualizeTimeLag_Object = MibScalar
dcEqualizeTimeLag = _DcEqualizeTimeLag_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 4, 4, 5),
    _DcEqualizeTimeLag_Type()
)
dcEqualizeTimeLag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcEqualizeTimeLag.setStatus("current")
if mibBuilder.loadTexts:
    dcEqualizeTimeLag.setUnits("minutes")
_DcEqualizeInterval_Type = Gauge32
_DcEqualizeInterval_Object = MibScalar
dcEqualizeInterval = _DcEqualizeInterval_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 4, 4, 6),
    _DcEqualizeInterval_Type()
)
dcEqualizeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcEqualizeInterval.setStatus("current")
if mibBuilder.loadTexts:
    dcEqualizeInterval.setUnits("days")


class _DcEqualizeStartTimeIntervalFrom_Type(DisplayString):
    """Custom type dcEqualizeStartTimeIntervalFrom based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_DcEqualizeStartTimeIntervalFrom_Type.__name__ = "DisplayString"
_DcEqualizeStartTimeIntervalFrom_Object = MibScalar
dcEqualizeStartTimeIntervalFrom = _DcEqualizeStartTimeIntervalFrom_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 4, 4, 7),
    _DcEqualizeStartTimeIntervalFrom_Type()
)
dcEqualizeStartTimeIntervalFrom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcEqualizeStartTimeIntervalFrom.setStatus("current")


class _DcEqualizeStartTimeIntervalTo_Type(DisplayString):
    """Custom type dcEqualizeStartTimeIntervalTo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_DcEqualizeStartTimeIntervalTo_Type.__name__ = "DisplayString"
_DcEqualizeStartTimeIntervalTo_Object = MibScalar
dcEqualizeStartTimeIntervalTo = _DcEqualizeStartTimeIntervalTo_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 4, 4, 8),
    _DcEqualizeStartTimeIntervalTo_Type()
)
dcEqualizeStartTimeIntervalTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcEqualizeStartTimeIntervalTo.setStatus("current")
_DcEqualizeInhibitAfterBoost_Type = Gauge32
_DcEqualizeInhibitAfterBoost_Object = MibScalar
dcEqualizeInhibitAfterBoost = _DcEqualizeInhibitAfterBoost_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 4, 4, 9),
    _DcEqualizeInhibitAfterBoost_Type()
)
dcEqualizeInhibitAfterBoost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcEqualizeInhibitAfterBoost.setStatus("current")
if mibBuilder.loadTexts:
    dcEqualizeInhibitAfterBoost.setUnits("hours")
_DcBoostCharge_ObjectIdentity = ObjectIdentity
dcBoostCharge = _DcBoostCharge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 5)
)


class _DcBoostChargeControl_Type(Integer32):
    """Custom type dcBoostChargeControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("start", 1),
          ("stop", 2))
    )


_DcBoostChargeControl_Type.__name__ = "Integer32"
_DcBoostChargeControl_Object = MibScalar
dcBoostChargeControl = _DcBoostChargeControl_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 5, 1),
    _DcBoostChargeControl_Type()
)
dcBoostChargeControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcBoostChargeControl.setStatus("current")


class _DcBoostChargeStatus_Type(Integer32):
    """Custom type dcBoostChargeStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 1),
          ("starting", 2),
          ("stopping", 3),
          ("cooking", 4),
          ("recovering", 5))
    )


_DcBoostChargeStatus_Type.__name__ = "Integer32"
_DcBoostChargeStatus_Object = MibScalar
dcBoostChargeStatus = _DcBoostChargeStatus_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 5, 2),
    _DcBoostChargeStatus_Type()
)
dcBoostChargeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcBoostChargeStatus.setStatus("current")


class _DcBoostChargeType_Type(Integer32):
    """Custom type dcBoostChargeType based on Integer32"""
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
        *(("none", 1),
          ("currentBased", 2),
          ("timeBased", 3),
          ("energyBased", 4))
    )


_DcBoostChargeType_Type.__name__ = "Integer32"
_DcBoostChargeType_Object = MibScalar
dcBoostChargeType = _DcBoostChargeType_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 5, 3),
    _DcBoostChargeType_Type()
)
dcBoostChargeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcBoostChargeType.setStatus("current")
_DcBoostChargeParameter_ObjectIdentity = ObjectIdentity
dcBoostChargeParameter = _DcBoostChargeParameter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 5, 4)
)
_DcBoostChargeVoltage_Type = Integer32
_DcBoostChargeVoltage_Object = MibScalar
dcBoostChargeVoltage = _DcBoostChargeVoltage_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 5, 4, 1),
    _DcBoostChargeVoltage_Type()
)
dcBoostChargeVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcBoostChargeVoltage.setStatus("current")
if mibBuilder.loadTexts:
    dcBoostChargeVoltage.setUnits("10 mV")
_DcBoostChargeMaxDuration_Type = Gauge32
_DcBoostChargeMaxDuration_Object = MibScalar
dcBoostChargeMaxDuration = _DcBoostChargeMaxDuration_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 5, 4, 2),
    _DcBoostChargeMaxDuration_Type()
)
dcBoostChargeMaxDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcBoostChargeMaxDuration.setStatus("current")
if mibBuilder.loadTexts:
    dcBoostChargeMaxDuration.setUnits("hours")


class _DcBoostChargeUseBattRoomFanEnabled_Type(Integer32):
    """Custom type dcBoostChargeUseBattRoomFanEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_DcBoostChargeUseBattRoomFanEnabled_Type.__name__ = "Integer32"
_DcBoostChargeUseBattRoomFanEnabled_Object = MibScalar
dcBoostChargeUseBattRoomFanEnabled = _DcBoostChargeUseBattRoomFanEnabled_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 5, 4, 3),
    _DcBoostChargeUseBattRoomFanEnabled_Type()
)
dcBoostChargeUseBattRoomFanEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcBoostChargeUseBattRoomFanEnabled.setStatus("current")
_DcBoostChargeTimeLag_Type = Gauge32
_DcBoostChargeTimeLag_Object = MibScalar
dcBoostChargeTimeLag = _DcBoostChargeTimeLag_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 5, 4, 4),
    _DcBoostChargeTimeLag_Type()
)
dcBoostChargeTimeLag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcBoostChargeTimeLag.setStatus("current")
if mibBuilder.loadTexts:
    dcBoostChargeTimeLag.setUnits("minutes")
_DcBoostChargeIstart_Type = Integer32
_DcBoostChargeIstart_Object = MibScalar
dcBoostChargeIstart = _DcBoostChargeIstart_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 5, 4, 5),
    _DcBoostChargeIstart_Type()
)
dcBoostChargeIstart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcBoostChargeIstart.setStatus("current")
if mibBuilder.loadTexts:
    dcBoostChargeIstart.setUnits("100 mA")
_DcBoostChargeIstop_Type = Integer32
_DcBoostChargeIstop_Object = MibScalar
dcBoostChargeIstop = _DcBoostChargeIstop_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 5, 4, 6),
    _DcBoostChargeIstop_Type()
)
dcBoostChargeIstop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcBoostChargeIstop.setStatus("current")
if mibBuilder.loadTexts:
    dcBoostChargeIstop.setUnits("100 mA")
_DcBoostChargeInhibitTime_Type = Gauge32
_DcBoostChargeInhibitTime_Object = MibScalar
dcBoostChargeInhibitTime = _DcBoostChargeInhibitTime_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 5, 4, 7),
    _DcBoostChargeInhibitTime_Type()
)
dcBoostChargeInhibitTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcBoostChargeInhibitTime.setStatus("current")
if mibBuilder.loadTexts:
    dcBoostChargeInhibitTime.setUnits("hours")
_DcSystemVoltageSupervision_ObjectIdentity = ObjectIdentity
dcSystemVoltageSupervision = _DcSystemVoltageSupervision_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 6)
)
_DcUaMax_Type = Integer32
_DcUaMax_Object = MibScalar
dcUaMax = _DcUaMax_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 6, 1),
    _DcUaMax_Type()
)
dcUaMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcUaMax.setStatus("current")
if mibBuilder.loadTexts:
    dcUaMax.setUnits("10 mV")
_DcUaMin_Type = Integer32
_DcUaMin_Object = MibScalar
dcUaMin = _DcUaMin_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 6, 2),
    _DcUaMin_Type()
)
dcUaMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcUaMin.setStatus("current")
if mibBuilder.loadTexts:
    dcUaMin.setUnits("10 mV")
_DcUsMax_Type = Integer32
_DcUsMax_Object = MibScalar
dcUsMax = _DcUsMax_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 6, 3),
    _DcUsMax_Type()
)
dcUsMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcUsMax.setStatus("current")
if mibBuilder.loadTexts:
    dcUsMax.setUnits("10 mV")
_DcUsMin_Type = Integer32
_DcUsMin_Object = MibScalar
dcUsMin = _DcUsMin_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 6, 4),
    _DcUsMin_Type()
)
dcUsMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcUsMin.setStatus("current")
if mibBuilder.loadTexts:
    dcUsMin.setUnits("10 mV")
_DcBoD_Type = Integer32
_DcBoD_Object = MibScalar
dcBoD = _DcBoD_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 6, 5),
    _DcBoD_Type()
)
dcBoD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcBoD.setStatus("current")
if mibBuilder.loadTexts:
    dcBoD.setUnits("10 mV")
_DcHysteresis_Type = Integer32
_DcHysteresis_Object = MibScalar
dcHysteresis = _DcHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 6, 6),
    _DcHysteresis_Type()
)
dcHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcHysteresis.setStatus("current")
if mibBuilder.loadTexts:
    dcHysteresis.setUnits("10 mV")


class _DcSuppressUaLowEnabled_Type(Integer32):
    """Custom type dcSuppressUaLowEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_DcSuppressUaLowEnabled_Type.__name__ = "Integer32"
_DcSuppressUaLowEnabled_Object = MibScalar
dcSuppressUaLowEnabled = _DcSuppressUaLowEnabled_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 6, 7),
    _DcSuppressUaLowEnabled_Type()
)
dcSuppressUaLowEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcSuppressUaLowEnabled.setStatus("current")


class _DcSuppressUsLowEnabled_Type(Integer32):
    """Custom type dcSuppressUsLowEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_DcSuppressUsLowEnabled_Type.__name__ = "Integer32"
_DcSuppressUsLowEnabled_Object = MibScalar
dcSuppressUsLowEnabled = _DcSuppressUsLowEnabled_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 6, 8),
    _DcSuppressUsLowEnabled_Type()
)
dcSuppressUsLowEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcSuppressUsLowEnabled.setStatus("current")


class _DcEnableUsTempComp_Type(Integer32):
    """Custom type dcEnableUsTempComp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_DcEnableUsTempComp_Type.__name__ = "Integer32"
_DcEnableUsTempComp_Object = MibScalar
dcEnableUsTempComp = _DcEnableUsTempComp_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 6, 9),
    _DcEnableUsTempComp_Type()
)
dcEnableUsTempComp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcEnableUsTempComp.setStatus("current")
_DcEvtCtrlCharge_ObjectIdentity = ObjectIdentity
dcEvtCtrlCharge = _DcEvtCtrlCharge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 7)
)


class _DcEvtCtrlChargeStatus_Type(Integer32):
    """Custom type dcEvtCtrlChargeStatus based on Integer32"""
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
        *(("inactive", 1),
          ("voltageControlled", 2),
          ("noBatteryCharge", 3),
          ("currentLimitation", 4))
    )


_DcEvtCtrlChargeStatus_Type.__name__ = "Integer32"
_DcEvtCtrlChargeStatus_Object = MibScalar
dcEvtCtrlChargeStatus = _DcEvtCtrlChargeStatus_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 7, 1),
    _DcEvtCtrlChargeStatus_Type()
)
dcEvtCtrlChargeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcEvtCtrlChargeStatus.setStatus("current")


class _DcEvtCtrlChargeType_Type(Integer32):
    """Custom type dcEvtCtrlChargeType based on Integer32"""
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
        *(("none", 1),
          ("voltageControlled", 2),
          ("noBatteryCharge", 3),
          ("currentLimitation", 4))
    )


_DcEvtCtrlChargeType_Type.__name__ = "Integer32"
_DcEvtCtrlChargeType_Object = MibScalar
dcEvtCtrlChargeType = _DcEvtCtrlChargeType_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 7, 2),
    _DcEvtCtrlChargeType_Type()
)
dcEvtCtrlChargeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcEvtCtrlChargeType.setStatus("current")
_DcEvtCtrlChargeParameter_ObjectIdentity = ObjectIdentity
dcEvtCtrlChargeParameter = _DcEvtCtrlChargeParameter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 7, 3)
)
_DcEvtCtrlChargeVoltage_Type = Integer32
_DcEvtCtrlChargeVoltage_Object = MibScalar
dcEvtCtrlChargeVoltage = _DcEvtCtrlChargeVoltage_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 7, 3, 1),
    _DcEvtCtrlChargeVoltage_Type()
)
dcEvtCtrlChargeVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcEvtCtrlChargeVoltage.setStatus("current")
if mibBuilder.loadTexts:
    dcEvtCtrlChargeVoltage.setUnits("10 mV")


class _DcEvtCtrlChargeTempCompEnabled_Type(Integer32):
    """Custom type dcEvtCtrlChargeTempCompEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_DcEvtCtrlChargeTempCompEnabled_Type.__name__ = "Integer32"
_DcEvtCtrlChargeTempCompEnabled_Object = MibScalar
dcEvtCtrlChargeTempCompEnabled = _DcEvtCtrlChargeTempCompEnabled_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 7, 3, 2),
    _DcEvtCtrlChargeTempCompEnabled_Type()
)
dcEvtCtrlChargeTempCompEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcEvtCtrlChargeTempCompEnabled.setStatus("current")
_DcEvtCtrlChargeMaxIBatt_Type = Integer32
_DcEvtCtrlChargeMaxIBatt_Object = MibScalar
dcEvtCtrlChargeMaxIBatt = _DcEvtCtrlChargeMaxIBatt_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 7, 3, 3),
    _DcEvtCtrlChargeMaxIBatt_Type()
)
dcEvtCtrlChargeMaxIBatt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcEvtCtrlChargeMaxIBatt.setStatus("current")
if mibBuilder.loadTexts:
    dcEvtCtrlChargeMaxIBatt.setUnits("100 mA")
_DcTempComp_ObjectIdentity = ObjectIdentity
dcTempComp = _DcTempComp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 8)
)


class _DcTempCompType_Type(Integer32):
    """Custom type dcTempCompType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("linear", 2),
          ("multi-stage", 3))
    )


_DcTempCompType_Type.__name__ = "Integer32"
_DcTempCompType_Object = MibScalar
dcTempCompType = _DcTempCompType_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 8, 1),
    _DcTempCompType_Type()
)
dcTempCompType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcTempCompType.setStatus("current")
_DcSlope_Type = Integer32
_DcSlope_Object = MibScalar
dcSlope = _DcSlope_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 8, 2),
    _DcSlope_Type()
)
dcSlope.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcSlope.setStatus("current")
if mibBuilder.loadTexts:
    dcSlope.setUnits("-1 mV/C")
_DcStartTemp_Type = Integer32
_DcStartTemp_Object = MibScalar
dcStartTemp = _DcStartTemp_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 8, 3),
    _DcStartTemp_Type()
)
dcStartTemp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcStartTemp.setStatus("current")
if mibBuilder.loadTexts:
    dcStartTemp.setUnits("0.1 C")
_DcStopTemp_Type = Integer32
_DcStopTemp_Object = MibScalar
dcStopTemp = _DcStopTemp_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 8, 4),
    _DcStopTemp_Type()
)
dcStopTemp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcStopTemp.setStatus("current")
if mibBuilder.loadTexts:
    dcStopTemp.setUnits("0.1 C")
_DcMaxVoltage_Type = Integer32
_DcMaxVoltage_Object = MibScalar
dcMaxVoltage = _DcMaxVoltage_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 8, 5),
    _DcMaxVoltage_Type()
)
dcMaxVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcMaxVoltage.setStatus("current")
if mibBuilder.loadTexts:
    dcMaxVoltage.setUnits("10 mV")
_DcLowStopVoltage_Type = Integer32
_DcLowStopVoltage_Object = MibScalar
dcLowStopVoltage = _DcLowStopVoltage_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 8, 6),
    _DcLowStopVoltage_Type()
)
dcLowStopVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcLowStopVoltage.setStatus("current")
if mibBuilder.loadTexts:
    dcLowStopVoltage.setUnits("10 mV")
_DcLowStartTemp_Type = Integer32
_DcLowStartTemp_Object = MibScalar
dcLowStartTemp = _DcLowStartTemp_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 8, 7),
    _DcLowStartTemp_Type()
)
dcLowStartTemp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcLowStartTemp.setStatus("current")
if mibBuilder.loadTexts:
    dcLowStartTemp.setUnits("0.1 C")
_DcLowTempSlope_Type = Integer32
_DcLowTempSlope_Object = MibScalar
dcLowTempSlope = _DcLowTempSlope_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 8, 8),
    _DcLowTempSlope_Type()
)
dcLowTempSlope.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcLowTempSlope.setStatus("current")
if mibBuilder.loadTexts:
    dcLowTempSlope.setUnits("-1 mV/C")
_DcHighStartTemp_Type = Integer32
_DcHighStartTemp_Object = MibScalar
dcHighStartTemp = _DcHighStartTemp_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 8, 9),
    _DcHighStartTemp_Type()
)
dcHighStartTemp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcHighStartTemp.setStatus("current")
if mibBuilder.loadTexts:
    dcHighStartTemp.setUnits("0.1 C")
_DcHighTempSlope_Type = Integer32
_DcHighTempSlope_Object = MibScalar
dcHighTempSlope = _DcHighTempSlope_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 8, 10),
    _DcHighTempSlope_Type()
)
dcHighTempSlope.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcHighTempSlope.setStatus("current")
if mibBuilder.loadTexts:
    dcHighTempSlope.setUnits("-1 mV/C")
_DcHighStopVoltage_Type = Integer32
_DcHighStopVoltage_Object = MibScalar
dcHighStopVoltage = _DcHighStopVoltage_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 8, 11),
    _DcHighStopVoltage_Type()
)
dcHighStopVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcHighStopVoltage.setStatus("current")
if mibBuilder.loadTexts:
    dcHighStopVoltage.setUnits("10 mV")
_DcRunawayTemp_Type = Integer32
_DcRunawayTemp_Object = MibScalar
dcRunawayTemp = _DcRunawayTemp_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 8, 12),
    _DcRunawayTemp_Type()
)
dcRunawayTemp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcRunawayTemp.setStatus("current")
if mibBuilder.loadTexts:
    dcRunawayTemp.setUnits("0.1 C")
_DcRunawayVoltage_Type = Integer32
_DcRunawayVoltage_Object = MibScalar
dcRunawayVoltage = _DcRunawayVoltage_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 8, 13),
    _DcRunawayVoltage_Type()
)
dcRunawayVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcRunawayVoltage.setStatus("current")
if mibBuilder.loadTexts:
    dcRunawayVoltage.setUnits("10 mV")
_DcTempSupervision_ObjectIdentity = ObjectIdentity
dcTempSupervision = _DcTempSupervision_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 9)
)
_DcHighTemp_Type = Integer32
_DcHighTemp_Object = MibScalar
dcHighTemp = _DcHighTemp_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 9, 1),
    _DcHighTemp_Type()
)
dcHighTemp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcHighTemp.setStatus("current")
if mibBuilder.loadTexts:
    dcHighTemp.setUnits("0.1 C")
_DcHighTempHyst_Type = Integer32
_DcHighTempHyst_Object = MibScalar
dcHighTempHyst = _DcHighTempHyst_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 9, 2),
    _DcHighTempHyst_Type()
)
dcHighTempHyst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcHighTempHyst.setStatus("current")
if mibBuilder.loadTexts:
    dcHighTempHyst.setUnits("0.1 C")
_DcInputOutput_ObjectIdentity = ObjectIdentity
dcInputOutput = _DcInputOutput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 6)
)
_DcControlEventTable_Object = MibTable
dcControlEventTable = _DcControlEventTable_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 6, 1)
)
if mibBuilder.loadTexts:
    dcControlEventTable.setStatus("current")
_DcControlEventEntry_Object = MibTableRow
dcControlEventEntry = _DcControlEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 6, 1, 1)
)
dcControlEventEntry.setIndexNames(
    (0, "ORION-BASE-MIB", "dcControlEventIndex"),
)
if mibBuilder.loadTexts:
    dcControlEventEntry.setStatus("current")


class _DcControlEventIndex_Type(Integer32):
    """Custom type dcControlEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_DcControlEventIndex_Type.__name__ = "Integer32"
_DcControlEventIndex_Object = MibTableColumn
dcControlEventIndex = _DcControlEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 6, 1, 1, 1),
    _DcControlEventIndex_Type()
)
dcControlEventIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dcControlEventIndex.setStatus("current")


class _DcControlEventName_Type(DisplayString):
    """Custom type dcControlEventName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 35),
    )


_DcControlEventName_Type.__name__ = "DisplayString"
_DcControlEventName_Object = MibTableColumn
dcControlEventName = _DcControlEventName_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 6, 1, 1, 2),
    _DcControlEventName_Type()
)
dcControlEventName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcControlEventName.setStatus("current")
_DcControlEventIdentifier_Type = Gauge32
_DcControlEventIdentifier_Object = MibTableColumn
dcControlEventIdentifier = _DcControlEventIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 6, 1, 1, 3),
    _DcControlEventIdentifier_Type()
)
dcControlEventIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcControlEventIdentifier.setStatus("current")


class _DcControlEventValue_Type(Integer32):
    """Custom type dcControlEventValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_DcControlEventValue_Type.__name__ = "Integer32"
_DcControlEventValue_Object = MibTableColumn
dcControlEventValue = _DcControlEventValue_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 6, 1, 1, 4),
    _DcControlEventValue_Type()
)
dcControlEventValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcControlEventValue.setStatus("current")
_DcMisc_ObjectIdentity = ObjectIdentity
dcMisc = _DcMisc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 7)
)
_DcTrapDestinationTable_Object = MibTable
dcTrapDestinationTable = _DcTrapDestinationTable_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 7, 1)
)
if mibBuilder.loadTexts:
    dcTrapDestinationTable.setStatus("current")
_DcTrapDestinationEntry_Object = MibTableRow
dcTrapDestinationEntry = _DcTrapDestinationEntry_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 7, 1, 1)
)
dcTrapDestinationEntry.setIndexNames(
    (0, "ORION-BASE-MIB", "dcTrapDestinationIndex"),
)
if mibBuilder.loadTexts:
    dcTrapDestinationEntry.setStatus("current")


class _DcTrapDestinationIndex_Type(Integer32):
    """Custom type dcTrapDestinationIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_DcTrapDestinationIndex_Type.__name__ = "Integer32"
_DcTrapDestinationIndex_Object = MibTableColumn
dcTrapDestinationIndex = _DcTrapDestinationIndex_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 7, 1, 1, 1),
    _DcTrapDestinationIndex_Type()
)
dcTrapDestinationIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dcTrapDestinationIndex.setStatus("current")
_DcTrapDestinationIp_Type = IpAddress
_DcTrapDestinationIp_Object = MibTableColumn
dcTrapDestinationIp = _DcTrapDestinationIp_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 7, 1, 1, 2),
    _DcTrapDestinationIp_Type()
)
dcTrapDestinationIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcTrapDestinationIp.setStatus("current")
_DcTrapDestinationPort_Type = Gauge32
_DcTrapDestinationPort_Object = MibTableColumn
dcTrapDestinationPort = _DcTrapDestinationPort_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 7, 1, 1, 3),
    _DcTrapDestinationPort_Type()
)
dcTrapDestinationPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcTrapDestinationPort.setStatus("current")


class _DcFileProcessingStatus_Type(Integer32):
    """Custom type dcFileProcessingStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("idle", 1),
          ("inProgress", 2),
          ("successful", 3),
          ("error", 4),
          ("unknown", 5))
    )


_DcFileProcessingStatus_Type.__name__ = "Integer32"
_DcFileProcessingStatus_Object = MibScalar
dcFileProcessingStatus = _DcFileProcessingStatus_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 7, 2),
    _DcFileProcessingStatus_Type()
)
dcFileProcessingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcFileProcessingStatus.setStatus("current")


class _DcResendActiveAlarmTraps_Type(Integer32):
    """Custom type dcResendActiveAlarmTraps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("resend", 1)
    )


_DcResendActiveAlarmTraps_Type.__name__ = "Integer32"
_DcResendActiveAlarmTraps_Object = MibScalar
dcResendActiveAlarmTraps = _DcResendActiveAlarmTraps_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 7, 4),
    _DcResendActiveAlarmTraps_Type()
)
dcResendActiveAlarmTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcResendActiveAlarmTraps.setStatus("current")
_DcConfig_ObjectIdentity = ObjectIdentity
dcConfig = _DcConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 8)
)
_DcDefaultLogEventTable_Object = MibTable
dcDefaultLogEventTable = _DcDefaultLogEventTable_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 8, 1)
)
if mibBuilder.loadTexts:
    dcDefaultLogEventTable.setStatus("current")
_DcDefaultLogEventEntry_Object = MibTableRow
dcDefaultLogEventEntry = _DcDefaultLogEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 8, 1, 1)
)
dcDefaultLogEventEntry.setIndexNames(
    (0, "ORION-BASE-MIB", "dcDefaultLogEventIndex"),
)
if mibBuilder.loadTexts:
    dcDefaultLogEventEntry.setStatus("current")


class _DcDefaultLogEventIndex_Type(Integer32):
    """Custom type dcDefaultLogEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_DcDefaultLogEventIndex_Type.__name__ = "Integer32"
_DcDefaultLogEventIndex_Object = MibTableColumn
dcDefaultLogEventIndex = _DcDefaultLogEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 8, 1, 1, 1),
    _DcDefaultLogEventIndex_Type()
)
dcDefaultLogEventIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dcDefaultLogEventIndex.setStatus("current")


class _DcDefaultLogEventName_Type(DisplayString):
    """Custom type dcDefaultLogEventName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 35),
    )


_DcDefaultLogEventName_Type.__name__ = "DisplayString"
_DcDefaultLogEventName_Object = MibTableColumn
dcDefaultLogEventName = _DcDefaultLogEventName_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 8, 1, 1, 2),
    _DcDefaultLogEventName_Type()
)
dcDefaultLogEventName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcDefaultLogEventName.setStatus("current")


class _DcDefaultLogEventLogged_Type(Integer32):
    """Custom type dcDefaultLogEventLogged based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_DcDefaultLogEventLogged_Type.__name__ = "Integer32"
_DcDefaultLogEventLogged_Object = MibTableColumn
dcDefaultLogEventLogged = _DcDefaultLogEventLogged_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 8, 1, 1, 3),
    _DcDefaultLogEventLogged_Type()
)
dcDefaultLogEventLogged.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcDefaultLogEventLogged.setStatus("current")
_DcEventProcessingEventTable_Object = MibTable
dcEventProcessingEventTable = _DcEventProcessingEventTable_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 8, 2)
)
if mibBuilder.loadTexts:
    dcEventProcessingEventTable.setStatus("current")
_DcEventProcessingEventEntry_Object = MibTableRow
dcEventProcessingEventEntry = _DcEventProcessingEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 8, 2, 1)
)
dcEventProcessingEventEntry.setIndexNames(
    (0, "ORION-BASE-MIB", "dcEventProcessingEventIndex"),
)
if mibBuilder.loadTexts:
    dcEventProcessingEventEntry.setStatus("current")


class _DcEventProcessingEventIndex_Type(Integer32):
    """Custom type dcEventProcessingEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_DcEventProcessingEventIndex_Type.__name__ = "Integer32"
_DcEventProcessingEventIndex_Object = MibTableColumn
dcEventProcessingEventIndex = _DcEventProcessingEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 8, 2, 1, 1),
    _DcEventProcessingEventIndex_Type()
)
dcEventProcessingEventIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dcEventProcessingEventIndex.setStatus("current")


class _DcEventProcessingEventName_Type(DisplayString):
    """Custom type dcEventProcessingEventName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 35),
    )


_DcEventProcessingEventName_Type.__name__ = "DisplayString"
_DcEventProcessingEventName_Object = MibTableColumn
dcEventProcessingEventName = _DcEventProcessingEventName_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 8, 2, 1, 2),
    _DcEventProcessingEventName_Type()
)
dcEventProcessingEventName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcEventProcessingEventName.setStatus("current")


class _DcEventProcessingEventAssigned_Type(Integer32):
    """Custom type dcEventProcessingEventAssigned based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_DcEventProcessingEventAssigned_Type.__name__ = "Integer32"
_DcEventProcessingEventAssigned_Object = MibTableColumn
dcEventProcessingEventAssigned = _DcEventProcessingEventAssigned_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 8, 2, 1, 3),
    _DcEventProcessingEventAssigned_Type()
)
dcEventProcessingEventAssigned.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcEventProcessingEventAssigned.setStatus("current")


class _DcEventProcessingEventType_Type(Integer32):
    """Custom type dcEventProcessingEventType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("eventOR", 2))
    )


_DcEventProcessingEventType_Type.__name__ = "Integer32"
_DcEventProcessingEventType_Object = MibTableColumn
dcEventProcessingEventType = _DcEventProcessingEventType_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 8, 2, 1, 4),
    _DcEventProcessingEventType_Type()
)
dcEventProcessingEventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcEventProcessingEventType.setStatus("current")
_DcEventProcessingEventSelected_Type = Gauge32
_DcEventProcessingEventSelected_Object = MibScalar
dcEventProcessingEventSelected = _DcEventProcessingEventSelected_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 8, 3),
    _DcEventProcessingEventSelected_Type()
)
dcEventProcessingEventSelected.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcEventProcessingEventSelected.setStatus("current")
_DcLvdTable_Object = MibTable
dcLvdTable = _DcLvdTable_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 8, 4)
)
if mibBuilder.loadTexts:
    dcLvdTable.setStatus("current")
_DcLvdEntry_Object = MibTableRow
dcLvdEntry = _DcLvdEntry_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 8, 4, 1)
)
dcLvdEntry.setIndexNames(
    (0, "ORION-BASE-MIB", "dcLvdIndex"),
)
if mibBuilder.loadTexts:
    dcLvdEntry.setStatus("current")


class _DcLvdIndex_Type(Integer32):
    """Custom type dcLvdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_DcLvdIndex_Type.__name__ = "Integer32"
_DcLvdIndex_Object = MibTableColumn
dcLvdIndex = _DcLvdIndex_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 8, 4, 1, 1),
    _DcLvdIndex_Type()
)
dcLvdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dcLvdIndex.setStatus("current")


class _DcLvdName_Type(DisplayString):
    """Custom type dcLvdName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_DcLvdName_Type.__name__ = "DisplayString"
_DcLvdName_Object = MibTableColumn
dcLvdName = _DcLvdName_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 8, 4, 1, 2),
    _DcLvdName_Type()
)
dcLvdName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcLvdName.setStatus("current")


class _DcLvdDisconnectDelay_Type(DisplayString):
    """Custom type dcLvdDisconnectDelay based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_DcLvdDisconnectDelay_Type.__name__ = "DisplayString"
_DcLvdDisconnectDelay_Object = MibTableColumn
dcLvdDisconnectDelay = _DcLvdDisconnectDelay_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 8, 4, 1, 3),
    _DcLvdDisconnectDelay_Type()
)
dcLvdDisconnectDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcLvdDisconnectDelay.setStatus("current")
_DcMeasurement_ObjectIdentity = ObjectIdentity
dcMeasurement = _DcMeasurement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 9)
)
_DcMeasurementTable_Object = MibTable
dcMeasurementTable = _DcMeasurementTable_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 9, 1)
)
if mibBuilder.loadTexts:
    dcMeasurementTable.setStatus("current")
_DcMeasurementEntry_Object = MibTableRow
dcMeasurementEntry = _DcMeasurementEntry_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 9, 1, 1)
)
dcMeasurementEntry.setIndexNames(
    (0, "ORION-BASE-MIB", "dcMeasurementIndex"),
)
if mibBuilder.loadTexts:
    dcMeasurementEntry.setStatus("current")


class _DcMeasurementIndex_Type(Integer32):
    """Custom type dcMeasurementIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 500),
    )


_DcMeasurementIndex_Type.__name__ = "Integer32"
_DcMeasurementIndex_Object = MibTableColumn
dcMeasurementIndex = _DcMeasurementIndex_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 9, 1, 1, 1),
    _DcMeasurementIndex_Type()
)
dcMeasurementIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dcMeasurementIndex.setStatus("current")


class _DcMeasurementName_Type(DisplayString):
    """Custom type dcMeasurementName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_DcMeasurementName_Type.__name__ = "DisplayString"
_DcMeasurementName_Object = MibTableColumn
dcMeasurementName = _DcMeasurementName_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 9, 1, 1, 2),
    _DcMeasurementName_Type()
)
dcMeasurementName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcMeasurementName.setStatus("current")
_DcMeasurementValue_Type = Integer32
_DcMeasurementValue_Object = MibTableColumn
dcMeasurementValue = _DcMeasurementValue_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 9, 1, 1, 3),
    _DcMeasurementValue_Type()
)
dcMeasurementValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcMeasurementValue.setStatus("current")
_DcMeasurementScaleFactor_Type = Integer32
_DcMeasurementScaleFactor_Object = MibTableColumn
dcMeasurementScaleFactor = _DcMeasurementScaleFactor_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 9, 1, 1, 4),
    _DcMeasurementScaleFactor_Type()
)
dcMeasurementScaleFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcMeasurementScaleFactor.setStatus("current")


class _DcMeasurementUnit_Type(Integer32):
    """Custom type dcMeasurementUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
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
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("none", 2),
          ("voltDC", 3),
          ("voltAC", 4),
          ("ampere", 5),
          ("ampereHour", 6),
          ("degreeCelsius", 7),
          ("temperatureCoefficient", 8),
          ("watt", 9),
          ("wattHour", 10),
          ("seconds", 11),
          ("percent", 12),
          ("hertz", 13),
          ("voltAmpere", 14),
          ("voltAmpereReactive", 15),
          ("voltAmpereReactiveHour", 16))
    )


_DcMeasurementUnit_Type.__name__ = "Integer32"
_DcMeasurementUnit_Object = MibTableColumn
dcMeasurementUnit = _DcMeasurementUnit_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 9, 1, 1, 5),
    _DcMeasurementUnit_Type()
)
dcMeasurementUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcMeasurementUnit.setStatus("current")
_DcMeterPanel_ObjectIdentity = ObjectIdentity
dcMeterPanel = _DcMeterPanel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 10)
)
_DcMeterPanelEventTable_Object = MibTable
dcMeterPanelEventTable = _DcMeterPanelEventTable_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 10, 1)
)
if mibBuilder.loadTexts:
    dcMeterPanelEventTable.setStatus("current")
_DcMeterPanelEventEntry_Object = MibTableRow
dcMeterPanelEventEntry = _DcMeterPanelEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 10, 1, 1)
)
dcMeterPanelEventEntry.setIndexNames(
    (0, "ORION-BASE-MIB", "dcMeterPanelEventIndex"),
)
if mibBuilder.loadTexts:
    dcMeterPanelEventEntry.setStatus("current")


class _DcMeterPanelEventIndex_Type(Integer32):
    """Custom type dcMeterPanelEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_DcMeterPanelEventIndex_Type.__name__ = "Integer32"
_DcMeterPanelEventIndex_Object = MibTableColumn
dcMeterPanelEventIndex = _DcMeterPanelEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 10, 1, 1, 1),
    _DcMeterPanelEventIndex_Type()
)
dcMeterPanelEventIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dcMeterPanelEventIndex.setStatus("current")


class _DcMeterPanelEventName_Type(DisplayString):
    """Custom type dcMeterPanelEventName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_DcMeterPanelEventName_Type.__name__ = "DisplayString"
_DcMeterPanelEventName_Object = MibTableColumn
dcMeterPanelEventName = _DcMeterPanelEventName_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 10, 1, 1, 2),
    _DcMeterPanelEventName_Type()
)
dcMeterPanelEventName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcMeterPanelEventName.setStatus("current")


class _DcMeterPanelEventValue_Type(Integer32):
    """Custom type dcMeterPanelEventValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("indeterminate", 2),
          ("true", 3))
    )


_DcMeterPanelEventValue_Type.__name__ = "Integer32"
_DcMeterPanelEventValue_Object = MibTableColumn
dcMeterPanelEventValue = _DcMeterPanelEventValue_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 10, 1, 1, 3),
    _DcMeterPanelEventValue_Type()
)
dcMeterPanelEventValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcMeterPanelEventValue.setStatus("current")
_DcMeterPanelEventHourMeterValue_Type = Gauge32
_DcMeterPanelEventHourMeterValue_Object = MibTableColumn
dcMeterPanelEventHourMeterValue = _DcMeterPanelEventHourMeterValue_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 10, 1, 1, 4),
    _DcMeterPanelEventHourMeterValue_Type()
)
dcMeterPanelEventHourMeterValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcMeterPanelEventHourMeterValue.setStatus("current")
if mibBuilder.loadTexts:
    dcMeterPanelEventHourMeterValue.setUnits("hours")
_ControllerEvents_ObjectIdentity = ObjectIdentity
controllerEvents = _ControllerEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 3)
)
_ControllerEventObjects_ObjectIdentity = ObjectIdentity
controllerEventObjects = _ControllerEventObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 3, 1)
)
_ControllerEventsV2_ObjectIdentity = ObjectIdentity
controllerEventsV2 = _ControllerEventsV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 3, 1, 0)
)

# Managed Objects groups

systemInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 1, 1, 1)
)
systemInfoGroup.setObjects(
      *(("ORION-BASE-MIB", "dcSiteName"),
        ("ORION-BASE-MIB", "dcSystemName"),
        ("ORION-BASE-MIB", "dcSystemDateTime"),
        ("ORION-BASE-MIB", "dcSoftwareVersion"))
)
if mibBuilder.loadTexts:
    systemInfoGroup.setStatus("current")

systemAlarmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 1, 1, 2)
)
systemAlarmGroup.setObjects(
      *(("ORION-BASE-MIB", "dcNumberUrgentAlarms"),
        ("ORION-BASE-MIB", "dcNumberNonUrgentAlarms"),
        ("ORION-BASE-MIB", "dcMainsFailureAlarm"),
        ("ORION-BASE-MIB", "dcUrgentAlarmIdentifier"),
        ("ORION-BASE-MIB", "dcUrgentAlarmValue"),
        ("ORION-BASE-MIB", "dcNonUrgentAlarmIdentifier"),
        ("ORION-BASE-MIB", "dcNonUrgentAlarmValue"),
        ("ORION-BASE-MIB", "dcUrgentAlarmName"),
        ("ORION-BASE-MIB", "dcNonUrgentAlarmName"),
        ("ORION-BASE-MIB", "dcNumberCriticalAlarms"),
        ("ORION-BASE-MIB", "dcCriticalAlarmIdentifier"),
        ("ORION-BASE-MIB", "dcCriticalAlarmValue"),
        ("ORION-BASE-MIB", "dcCriticalAlarmName"))
)
if mibBuilder.loadTexts:
    systemAlarmGroup.setStatus("current")

systemMonitorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 1, 1, 3)
)
systemMonitorGroup.setObjects(
      *(("ORION-BASE-MIB", "dcSystemVoltage"),
        ("ORION-BASE-MIB", "dcLoadCurrent"),
        ("ORION-BASE-MIB", "dcBatteryCurrent"),
        ("ORION-BASE-MIB", "dcBatteryTemperature"),
        ("ORION-BASE-MIB", "dcChargeState"),
        ("ORION-BASE-MIB", "dcCurrentLimit"),
        ("ORION-BASE-MIB", "dcRectifierCurrent"),
        ("ORION-BASE-MIB", "dcSystemPower"))
)
if mibBuilder.loadTexts:
    systemMonitorGroup.setStatus("current")

rectifierGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 1, 1, 4)
)
rectifierGroup.setObjects(
      *(("ORION-BASE-MIB", "dcNumberRectifiers"),
        ("ORION-BASE-MIB", "dcNumberRectifiersFailure"),
        ("ORION-BASE-MIB", "dcNumberRectifiersOkay"),
        ("ORION-BASE-MIB", "dcEfficiencyCyclingEnabled"),
        ("ORION-BASE-MIB", "dcLimitSwitchingTimes"),
        ("ORION-BASE-MIB", "dcForceSwitchingOncePerMonth"),
        ("ORION-BASE-MIB", "dcMaximumLoadStep"),
        ("ORION-BASE-MIB", "dcMinimumLoadStep"))
)
if mibBuilder.loadTexts:
    rectifierGroup.setStatus("current")

eventHistoryTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 1, 1, 5)
)
eventHistoryTableGroup.setObjects(
      *(("ORION-BASE-MIB", "dcEventHistoryTimestamp"),
        ("ORION-BASE-MIB", "dcEventHistoryMessage"))
)
if mibBuilder.loadTexts:
    eventHistoryTableGroup.setStatus("current")

alarmTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 1, 1, 6)
)
alarmTableGroup.setObjects(
      *(("ORION-BASE-MIB", "dcAlarmEventCategory"),
        ("ORION-BASE-MIB", "dcAlarmEventName"),
        ("ORION-BASE-MIB", "dcAlarmEventIdentifier"),
        ("ORION-BASE-MIB", "dcAlarmEventValue"))
)
if mibBuilder.loadTexts:
    alarmTableGroup.setStatus("current")

rectifierTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 1, 1, 7)
)
rectifierTableGroup.setObjects(
      *(("ORION-BASE-MIB", "dcRectifierIdentifier"),
        ("ORION-BASE-MIB", "dcRectifierStatus"))
)
if mibBuilder.loadTexts:
    rectifierTableGroup.setStatus("current")

genericAlarmTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 1, 1, 9)
)
genericAlarmTableGroup.setObjects(
      *(("ORION-BASE-MIB", "dcGenericAlarmEventIdentifier"),
        ("ORION-BASE-MIB", "dcGenericAlarmEventName"),
        ("ORION-BASE-MIB", "dcGenericAlarmEventValue"))
)
if mibBuilder.loadTexts:
    genericAlarmTableGroup.setStatus("current")

batteryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 1, 1, 10)
)
batteryGroup.setObjects(
      *(("ORION-BASE-MIB", "dcUsys20"),
        ("ORION-BASE-MIB", "dcTempCompType"),
        ("ORION-BASE-MIB", "dcSlope"),
        ("ORION-BASE-MIB", "dcStartTemp"),
        ("ORION-BASE-MIB", "dcStopTemp"),
        ("ORION-BASE-MIB", "dcMaxVoltage"),
        ("ORION-BASE-MIB", "dcLowStopVoltage"),
        ("ORION-BASE-MIB", "dcLowStartTemp"),
        ("ORION-BASE-MIB", "dcLowTempSlope"),
        ("ORION-BASE-MIB", "dcHighStartTemp"),
        ("ORION-BASE-MIB", "dcHighTempSlope"),
        ("ORION-BASE-MIB", "dcHighStopVoltage"),
        ("ORION-BASE-MIB", "dcRunawayTemp"),
        ("ORION-BASE-MIB", "dcRunawayVoltage"),
        ("ORION-BASE-MIB", "dcBatteryTestUsupport"),
        ("ORION-BASE-MIB", "dcBatteryTestDuration"),
        ("ORION-BASE-MIB", "dcBatteryTestInterval"),
        ("ORION-BASE-MIB", "dcBatteryTestDischargeCurrent"),
        ("ORION-BASE-MIB", "dcBatteryTestMinDuration"),
        ("ORION-BASE-MIB", "dcBatteryTestVoltageWithinUfloat"),
        ("ORION-BASE-MIB", "dcBatteryTestVoltageWithinUfloatPeriod"),
        ("ORION-BASE-MIB", "dcBatteryTestTempFrom"),
        ("ORION-BASE-MIB", "dcBatteryTestTempTo"),
        ("ORION-BASE-MIB", "dcBatteryTestIntervalEnabled"),
        ("ORION-BASE-MIB", "dcBatteryTestStartTimeFrom"),
        ("ORION-BASE-MIB", "dcBatteryTestStartTimeTo"),
        ("ORION-BASE-MIB", "dcBatteryTestDateTime"),
        ("ORION-BASE-MIB", "dcBatteryTestResult"),
        ("ORION-BASE-MIB", "dcBatteryTestEndVoltage"),
        ("ORION-BASE-MIB", "dcBatteryTestControl"),
        ("ORION-BASE-MIB", "dcBatteryTestStatus"),
        ("ORION-BASE-MIB", "dcBatteryTestFailureEvent"),
        ("ORION-BASE-MIB", "dcBatteryTestType"),
        ("ORION-BASE-MIB", "dcTotalBatteryCapacity"),
        ("ORION-BASE-MIB", "dcLossOfBackupTimeEnabled"),
        ("ORION-BASE-MIB", "dcLossOfBackupTimeStatus"),
        ("ORION-BASE-MIB", "dcExpectedBackupTime"),
        ("ORION-BASE-MIB", "dcEqualizeControl"),
        ("ORION-BASE-MIB", "dcEqualizeStatus"),
        ("ORION-BASE-MIB", "dcEqualizeEnabled"),
        ("ORION-BASE-MIB", "dcEqualizeVoltage"),
        ("ORION-BASE-MIB", "dcEqualizeDuration"),
        ("ORION-BASE-MIB", "dcEqualizeUseBattRoomFanEnabled"),
        ("ORION-BASE-MIB", "dcEqualizeLeadTime"),
        ("ORION-BASE-MIB", "dcEqualizeTimeLag"),
        ("ORION-BASE-MIB", "dcEqualizeInterval"),
        ("ORION-BASE-MIB", "dcEqualizeStartTimeIntervalFrom"),
        ("ORION-BASE-MIB", "dcEqualizeStartTimeIntervalTo"),
        ("ORION-BASE-MIB", "dcEqualizeInhibitAfterBoost"),
        ("ORION-BASE-MIB", "dcBoostChargeControl"),
        ("ORION-BASE-MIB", "dcBoostChargeStatus"),
        ("ORION-BASE-MIB", "dcBoostChargeType"),
        ("ORION-BASE-MIB", "dcBoostChargeVoltage"),
        ("ORION-BASE-MIB", "dcBoostChargeMaxDuration"),
        ("ORION-BASE-MIB", "dcBoostChargeUseBattRoomFanEnabled"),
        ("ORION-BASE-MIB", "dcBoostChargeTimeLag"),
        ("ORION-BASE-MIB", "dcBoostChargeIstart"),
        ("ORION-BASE-MIB", "dcBoostChargeIstop"),
        ("ORION-BASE-MIB", "dcBoostChargeInhibitTime"),
        ("ORION-BASE-MIB", "dcUaMax"),
        ("ORION-BASE-MIB", "dcUaMin"),
        ("ORION-BASE-MIB", "dcUsMax"),
        ("ORION-BASE-MIB", "dcUsMin"),
        ("ORION-BASE-MIB", "dcBoD"),
        ("ORION-BASE-MIB", "dcHysteresis"),
        ("ORION-BASE-MIB", "dcSuppressUaLowEnabled"),
        ("ORION-BASE-MIB", "dcSuppressUsLowEnabled"),
        ("ORION-BASE-MIB", "dcEnableUsTempComp"),
        ("ORION-BASE-MIB", "dcEvtCtrlChargeStatus"),
        ("ORION-BASE-MIB", "dcEvtCtrlChargeType"),
        ("ORION-BASE-MIB", "dcEvtCtrlChargeVoltage"),
        ("ORION-BASE-MIB", "dcEvtCtrlChargeTempCompEnabled"),
        ("ORION-BASE-MIB", "dcEvtCtrlChargeMaxIBatt"),
        ("ORION-BASE-MIB", "dcHighTemp"),
        ("ORION-BASE-MIB", "dcHighTempHyst"))
)
if mibBuilder.loadTexts:
    batteryGroup.setStatus("current")

controlEventTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 1, 1, 11)
)
controlEventTableGroup.setObjects(
      *(("ORION-BASE-MIB", "dcControlEventName"),
        ("ORION-BASE-MIB", "dcControlEventIdentifier"),
        ("ORION-BASE-MIB", "dcControlEventValue"))
)
if mibBuilder.loadTexts:
    controlEventTableGroup.setStatus("current")

trapDestinationTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 1, 1, 12)
)
trapDestinationTableGroup.setObjects(
      *(("ORION-BASE-MIB", "dcTrapDestinationIp"),
        ("ORION-BASE-MIB", "dcTrapDestinationPort"))
)
if mibBuilder.loadTexts:
    trapDestinationTableGroup.setStatus("current")

miscGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 1, 1, 13)
)
miscGroup.setObjects(
      *(("ORION-BASE-MIB", "dcFileProcessingStatus"),
        ("ORION-BASE-MIB", "dcResendActiveAlarmTraps"))
)
if mibBuilder.loadTexts:
    miscGroup.setStatus("current")

rectifierGroupTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 1, 1, 14)
)
rectifierGroupTableGroup.setObjects(
      *(("ORION-BASE-MIB", "dcRectifierGroupName"),
        ("ORION-BASE-MIB", "dcRectifierGroupRectifierType"),
        ("ORION-BASE-MIB", "dcRectifierGroupDefaultVoltage"),
        ("ORION-BASE-MIB", "dcRectifierGroupDefaultCurrentLimit"),
        ("ORION-BASE-MIB", "dcRectifierGroupDefaultPowerLimit"),
        ("ORION-BASE-MIB", "dcRectifierGroupInputLowOff"),
        ("ORION-BASE-MIB", "dcRectifierGroupInputLowOn"),
        ("ORION-BASE-MIB", "dcRectifierGroupStartupVoltage"),
        ("ORION-BASE-MIB", "dcRectifierGroupStartupCurrentLimit"),
        ("ORION-BASE-MIB", "dcRectifierGroupStartupPowerLimit"),
        ("ORION-BASE-MIB", "dcRectifierGroupStartupTimeLimit"),
        ("ORION-BASE-MIB", "dcRectifierGroupPowerupDelay"),
        ("ORION-BASE-MIB", "dcRectifierGroupPowerupTime"),
        ("ORION-BASE-MIB", "dcRectifierGroupUmaxOff"))
)
if mibBuilder.loadTexts:
    rectifierGroupTableGroup.setStatus("current")

batteryStringTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 1, 1, 15)
)
batteryStringTableGroup.setObjects(
      *(("ORION-BASE-MIB", "dcBatteryStringName"),
        ("ORION-BASE-MIB", "dcBatteryStringMaxIBatt"),
        ("ORION-BASE-MIB", "dcBatteryStringCapacity"))
)
if mibBuilder.loadTexts:
    batteryStringTableGroup.setStatus("current")

defaultLogEventTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 1, 1, 16)
)
defaultLogEventTableGroup.setObjects(
      *(("ORION-BASE-MIB", "dcDefaultLogEventName"),
        ("ORION-BASE-MIB", "dcDefaultLogEventLogged"))
)
if mibBuilder.loadTexts:
    defaultLogEventTableGroup.setStatus("current")

eventProcessingEventTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 1, 1, 17)
)
eventProcessingEventTableGroup.setObjects(
      *(("ORION-BASE-MIB", "dcEventProcessingEventName"),
        ("ORION-BASE-MIB", "dcEventProcessingEventAssigned"),
        ("ORION-BASE-MIB", "dcEventProcessingEventType"),
        ("ORION-BASE-MIB", "dcEventProcessingEventSelected"))
)
if mibBuilder.loadTexts:
    eventProcessingEventTableGroup.setStatus("current")

lvdTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 1, 1, 18)
)
lvdTableGroup.setObjects(
      *(("ORION-BASE-MIB", "dcLvdName"),
        ("ORION-BASE-MIB", "dcLvdDisconnectDelay"))
)
if mibBuilder.loadTexts:
    lvdTableGroup.setStatus("current")

powerLimitationTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 1, 1, 19)
)
powerLimitationTableGroup.setObjects(
      *(("ORION-BASE-MIB", "dcPowerLimitationEventName"),
        ("ORION-BASE-MIB", "dcPowerLimitationStatus"),
        ("ORION-BASE-MIB", "dcPowerLimitationType"),
        ("ORION-BASE-MIB", "dcPowerLimitationLimit"),
        ("ORION-BASE-MIB", "dcPowerLimitationNoBatteryDischarge"))
)
if mibBuilder.loadTexts:
    powerLimitationTableGroup.setStatus("current")

measurementTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 1, 1, 20)
)
measurementTableGroup.setObjects(
      *(("ORION-BASE-MIB", "dcMeasurementName"),
        ("ORION-BASE-MIB", "dcMeasurementValue"),
        ("ORION-BASE-MIB", "dcMeasurementScaleFactor"),
        ("ORION-BASE-MIB", "dcMeasurementUnit"))
)
if mibBuilder.loadTexts:
    measurementTableGroup.setStatus("current")

meterPanelEventTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 1, 1, 21)
)
meterPanelEventTableGroup.setObjects(
      *(("ORION-BASE-MIB", "dcMeterPanelEventName"),
        ("ORION-BASE-MIB", "dcMeterPanelEventValue"),
        ("ORION-BASE-MIB", "dcMeterPanelEventHourMeterValue"))
)
if mibBuilder.loadTexts:
    meterPanelEventTableGroup.setStatus("current")


# Notification objects

systemNonUrgentAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 3, 1, 0, 1)
)
systemNonUrgentAlarm.setObjects(
      *(("ORION-BASE-MIB", "dcSystemDateTime"),
        ("ORION-BASE-MIB", "dcNumberNonUrgentAlarms"),
        ("ORION-BASE-MIB", "dcNonUrgentAlarmIdentifier"),
        ("ORION-BASE-MIB", "dcNonUrgentAlarmValue"),
        ("ORION-BASE-MIB", "dcNonUrgentAlarmName"))
)
if mibBuilder.loadTexts:
    systemNonUrgentAlarm.setStatus(
        "current"
    )

systemUrgentAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 3, 1, 0, 2)
)
systemUrgentAlarm.setObjects(
      *(("ORION-BASE-MIB", "dcSystemDateTime"),
        ("ORION-BASE-MIB", "dcNumberUrgentAlarms"),
        ("ORION-BASE-MIB", "dcUrgentAlarmIdentifier"),
        ("ORION-BASE-MIB", "dcUrgentAlarmValue"),
        ("ORION-BASE-MIB", "dcUrgentAlarmName"))
)
if mibBuilder.loadTexts:
    systemUrgentAlarm.setStatus(
        "current"
    )

systemCriticalAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 3, 1, 0, 3)
)
systemCriticalAlarm.setObjects(
      *(("ORION-BASE-MIB", "dcSystemDateTime"),
        ("ORION-BASE-MIB", "dcNumberCriticalAlarms"),
        ("ORION-BASE-MIB", "dcCriticalAlarmIdentifier"),
        ("ORION-BASE-MIB", "dcCriticalAlarmValue"),
        ("ORION-BASE-MIB", "dcCriticalAlarmName"))
)
if mibBuilder.loadTexts:
    systemCriticalAlarm.setStatus(
        "current"
    )


# Notifications groups

notificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 1, 1, 8)
)
notificationsGroup.setObjects(
      *(("ORION-BASE-MIB", "systemNonUrgentAlarm"),
        ("ORION-BASE-MIB", "systemUrgentAlarm"),
        ("ORION-BASE-MIB", "systemCriticalAlarm"))
)
if mibBuilder.loadTexts:
    notificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

controllerBasicCompl = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 1, 2, 1)
)
controllerBasicCompl.setObjects(
      *(("ORION-BASE-MIB", "systemInfoGroup"),
        ("ORION-BASE-MIB", "systemAlarmGroup"),
        ("ORION-BASE-MIB", "systemMonitorGroup"),
        ("ORION-BASE-MIB", "alarmTableGroup"),
        ("ORION-BASE-MIB", "notificationsGroup"))
)
if mibBuilder.loadTexts:
    controllerBasicCompl.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ORION-BASE-MIB",
    **{"orionBaseMibModule": orionBaseMibModule,
       "orionBaseMib": orionBaseMib,
       "controllerConfs": controllerConfs,
       "controllerGroups": controllerGroups,
       "systemInfoGroup": systemInfoGroup,
       "systemAlarmGroup": systemAlarmGroup,
       "systemMonitorGroup": systemMonitorGroup,
       "rectifierGroup": rectifierGroup,
       "eventHistoryTableGroup": eventHistoryTableGroup,
       "alarmTableGroup": alarmTableGroup,
       "rectifierTableGroup": rectifierTableGroup,
       "notificationsGroup": notificationsGroup,
       "genericAlarmTableGroup": genericAlarmTableGroup,
       "batteryGroup": batteryGroup,
       "controlEventTableGroup": controlEventTableGroup,
       "trapDestinationTableGroup": trapDestinationTableGroup,
       "miscGroup": miscGroup,
       "rectifierGroupTableGroup": rectifierGroupTableGroup,
       "batteryStringTableGroup": batteryStringTableGroup,
       "defaultLogEventTableGroup": defaultLogEventTableGroup,
       "eventProcessingEventTableGroup": eventProcessingEventTableGroup,
       "lvdTableGroup": lvdTableGroup,
       "powerLimitationTableGroup": powerLimitationTableGroup,
       "measurementTableGroup": measurementTableGroup,
       "meterPanelEventTableGroup": meterPanelEventTableGroup,
       "controllerCompl": controllerCompl,
       "controllerBasicCompl": controllerBasicCompl,
       "controllerObjects": controllerObjects,
       "dcSystemInfo": dcSystemInfo,
       "dcSiteName": dcSiteName,
       "dcSystemName": dcSystemName,
       "dcSystemDateTime": dcSystemDateTime,
       "dcSoftwareVersion": dcSoftwareVersion,
       "dcSystemAlarms": dcSystemAlarms,
       "dcEventHistoryTable": dcEventHistoryTable,
       "dcEventHistoryEntry": dcEventHistoryEntry,
       "dcEventHistoryIndex": dcEventHistoryIndex,
       "dcEventHistoryTimestamp": dcEventHistoryTimestamp,
       "dcEventHistoryMessage": dcEventHistoryMessage,
       "dcAlarmTable": dcAlarmTable,
       "dcAlarmEntry": dcAlarmEntry,
       "dcAlarmIndex": dcAlarmIndex,
       "dcAlarmEventCategory": dcAlarmEventCategory,
       "dcAlarmEventName": dcAlarmEventName,
       "dcAlarmEventIdentifier": dcAlarmEventIdentifier,
       "dcAlarmEventValue": dcAlarmEventValue,
       "dcNumberUrgentAlarms": dcNumberUrgentAlarms,
       "dcNumberNonUrgentAlarms": dcNumberNonUrgentAlarms,
       "dcMainsFailureAlarm": dcMainsFailureAlarm,
       "dcUrgentAlarmIdentifier": dcUrgentAlarmIdentifier,
       "dcUrgentAlarmValue": dcUrgentAlarmValue,
       "dcNonUrgentAlarmIdentifier": dcNonUrgentAlarmIdentifier,
       "dcNonUrgentAlarmValue": dcNonUrgentAlarmValue,
       "dcUrgentAlarmName": dcUrgentAlarmName,
       "dcNonUrgentAlarmName": dcNonUrgentAlarmName,
       "dcGenericAlarmTable": dcGenericAlarmTable,
       "dcGenericAlarmEntry": dcGenericAlarmEntry,
       "dcGenericAlarmIndex": dcGenericAlarmIndex,
       "dcGenericAlarmEventName": dcGenericAlarmEventName,
       "dcGenericAlarmEventIdentifier": dcGenericAlarmEventIdentifier,
       "dcGenericAlarmEventValue": dcGenericAlarmEventValue,
       "dcNumberCriticalAlarms": dcNumberCriticalAlarms,
       "dcCriticalAlarmIdentifier": dcCriticalAlarmIdentifier,
       "dcCriticalAlarmValue": dcCriticalAlarmValue,
       "dcCriticalAlarmName": dcCriticalAlarmName,
       "dcSystemMonitor": dcSystemMonitor,
       "dcSystemVoltage": dcSystemVoltage,
       "dcLoadCurrent": dcLoadCurrent,
       "dcBatteryCurrent": dcBatteryCurrent,
       "dcBatteryTemperature": dcBatteryTemperature,
       "dcChargeState": dcChargeState,
       "dcCurrentLimit": dcCurrentLimit,
       "dcRectifierCurrent": dcRectifierCurrent,
       "dcSystemPower": dcSystemPower,
       "dcRectifier": dcRectifier,
       "dcNumberRectifiers": dcNumberRectifiers,
       "dcNumberRectifiersFailure": dcNumberRectifiersFailure,
       "dcNumberRectifiersOkay": dcNumberRectifiersOkay,
       "dcRectifierTable": dcRectifierTable,
       "dcRectifierEntry": dcRectifierEntry,
       "dcRectifierIndex": dcRectifierIndex,
       "dcRectifierIdentifier": dcRectifierIdentifier,
       "dcRectifierStatus": dcRectifierStatus,
       "dcRectifierGroupTable": dcRectifierGroupTable,
       "dcRectifierGroupEntry": dcRectifierGroupEntry,
       "dcRectifierGroupIndex": dcRectifierGroupIndex,
       "dcRectifierGroupName": dcRectifierGroupName,
       "dcRectifierGroupRectifierType": dcRectifierGroupRectifierType,
       "dcRectifierGroupDefaultVoltage": dcRectifierGroupDefaultVoltage,
       "dcRectifierGroupDefaultCurrentLimit": dcRectifierGroupDefaultCurrentLimit,
       "dcRectifierGroupDefaultPowerLimit": dcRectifierGroupDefaultPowerLimit,
       "dcRectifierGroupInputLowOff": dcRectifierGroupInputLowOff,
       "dcRectifierGroupInputLowOn": dcRectifierGroupInputLowOn,
       "dcRectifierGroupStartupVoltage": dcRectifierGroupStartupVoltage,
       "dcRectifierGroupStartupCurrentLimit": dcRectifierGroupStartupCurrentLimit,
       "dcRectifierGroupStartupPowerLimit": dcRectifierGroupStartupPowerLimit,
       "dcRectifierGroupStartupTimeLimit": dcRectifierGroupStartupTimeLimit,
       "dcRectifierGroupPowerupDelay": dcRectifierGroupPowerupDelay,
       "dcRectifierGroupPowerupTime": dcRectifierGroupPowerupTime,
       "dcRectifierGroupUmaxOff": dcRectifierGroupUmaxOff,
       "dcRectifierFunctions": dcRectifierFunctions,
       "dcEfficiencyCycling": dcEfficiencyCycling,
       "dcEfficiencyCyclingEnabled": dcEfficiencyCyclingEnabled,
       "dcLimitSwitchingTimes": dcLimitSwitchingTimes,
       "dcForceSwitchingOncePerMonth": dcForceSwitchingOncePerMonth,
       "dcMaximumLoadStep": dcMaximumLoadStep,
       "dcMinimumLoadStep": dcMinimumLoadStep,
       "dcPowerLimitation": dcPowerLimitation,
       "dcPowerLimitationTable": dcPowerLimitationTable,
       "dcPowerLimitationEntry": dcPowerLimitationEntry,
       "dcPowerLimitationIndex": dcPowerLimitationIndex,
       "dcPowerLimitationEventName": dcPowerLimitationEventName,
       "dcPowerLimitationStatus": dcPowerLimitationStatus,
       "dcPowerLimitationType": dcPowerLimitationType,
       "dcPowerLimitationLimit": dcPowerLimitationLimit,
       "dcPowerLimitationNoBatteryDischarge": dcPowerLimitationNoBatteryDischarge,
       "dcBattery": dcBattery,
       "dcFloatCharge": dcFloatCharge,
       "dcUsys20": dcUsys20,
       "dcBatteryTest": dcBatteryTest,
       "dcBatteryTestParameter": dcBatteryTestParameter,
       "dcBatteryTestUsupport": dcBatteryTestUsupport,
       "dcBatteryTestDuration": dcBatteryTestDuration,
       "dcBatteryTestInterval": dcBatteryTestInterval,
       "dcBatteryTestDischargeCurrent": dcBatteryTestDischargeCurrent,
       "dcBatteryTestMinDuration": dcBatteryTestMinDuration,
       "dcBatteryTestVoltageWithinUfloat": dcBatteryTestVoltageWithinUfloat,
       "dcBatteryTestVoltageWithinUfloatPeriod": dcBatteryTestVoltageWithinUfloatPeriod,
       "dcBatteryTestTempFrom": dcBatteryTestTempFrom,
       "dcBatteryTestTempTo": dcBatteryTestTempTo,
       "dcBatteryTestIntervalEnabled": dcBatteryTestIntervalEnabled,
       "dcBatteryTestStartTimeFrom": dcBatteryTestStartTimeFrom,
       "dcBatteryTestStartTimeTo": dcBatteryTestStartTimeTo,
       "dcBatteryTestResults": dcBatteryTestResults,
       "dcBatteryTestDateTime": dcBatteryTestDateTime,
       "dcBatteryTestResult": dcBatteryTestResult,
       "dcBatteryTestEndVoltage": dcBatteryTestEndVoltage,
       "dcBatteryTestControl": dcBatteryTestControl,
       "dcBatteryTestStatus": dcBatteryTestStatus,
       "dcBatteryTestFailureEvent": dcBatteryTestFailureEvent,
       "dcBatteryTestType": dcBatteryTestType,
       "dcBatteryParameter": dcBatteryParameter,
       "dcTotalBatteryCapacity": dcTotalBatteryCapacity,
       "dcBatteryStringTable": dcBatteryStringTable,
       "dcBatteryStringEntry": dcBatteryStringEntry,
       "dcBatteryStringIndex": dcBatteryStringIndex,
       "dcBatteryStringName": dcBatteryStringName,
       "dcBatteryStringMaxIBatt": dcBatteryStringMaxIBatt,
       "dcBatteryStringCapacity": dcBatteryStringCapacity,
       "dcLossOfBackupTime": dcLossOfBackupTime,
       "dcLossOfBackupTimeEnabled": dcLossOfBackupTimeEnabled,
       "dcLossOfBackupTimeStatus": dcLossOfBackupTimeStatus,
       "dcExpectedBackupTime": dcExpectedBackupTime,
       "dcEqualize": dcEqualize,
       "dcEqualizeControl": dcEqualizeControl,
       "dcEqualizeStatus": dcEqualizeStatus,
       "dcEqualizeEnabled": dcEqualizeEnabled,
       "dcEqualizeParameter": dcEqualizeParameter,
       "dcEqualizeVoltage": dcEqualizeVoltage,
       "dcEqualizeDuration": dcEqualizeDuration,
       "dcEqualizeUseBattRoomFanEnabled": dcEqualizeUseBattRoomFanEnabled,
       "dcEqualizeLeadTime": dcEqualizeLeadTime,
       "dcEqualizeTimeLag": dcEqualizeTimeLag,
       "dcEqualizeInterval": dcEqualizeInterval,
       "dcEqualizeStartTimeIntervalFrom": dcEqualizeStartTimeIntervalFrom,
       "dcEqualizeStartTimeIntervalTo": dcEqualizeStartTimeIntervalTo,
       "dcEqualizeInhibitAfterBoost": dcEqualizeInhibitAfterBoost,
       "dcBoostCharge": dcBoostCharge,
       "dcBoostChargeControl": dcBoostChargeControl,
       "dcBoostChargeStatus": dcBoostChargeStatus,
       "dcBoostChargeType": dcBoostChargeType,
       "dcBoostChargeParameter": dcBoostChargeParameter,
       "dcBoostChargeVoltage": dcBoostChargeVoltage,
       "dcBoostChargeMaxDuration": dcBoostChargeMaxDuration,
       "dcBoostChargeUseBattRoomFanEnabled": dcBoostChargeUseBattRoomFanEnabled,
       "dcBoostChargeTimeLag": dcBoostChargeTimeLag,
       "dcBoostChargeIstart": dcBoostChargeIstart,
       "dcBoostChargeIstop": dcBoostChargeIstop,
       "dcBoostChargeInhibitTime": dcBoostChargeInhibitTime,
       "dcSystemVoltageSupervision": dcSystemVoltageSupervision,
       "dcUaMax": dcUaMax,
       "dcUaMin": dcUaMin,
       "dcUsMax": dcUsMax,
       "dcUsMin": dcUsMin,
       "dcBoD": dcBoD,
       "dcHysteresis": dcHysteresis,
       "dcSuppressUaLowEnabled": dcSuppressUaLowEnabled,
       "dcSuppressUsLowEnabled": dcSuppressUsLowEnabled,
       "dcEnableUsTempComp": dcEnableUsTempComp,
       "dcEvtCtrlCharge": dcEvtCtrlCharge,
       "dcEvtCtrlChargeStatus": dcEvtCtrlChargeStatus,
       "dcEvtCtrlChargeType": dcEvtCtrlChargeType,
       "dcEvtCtrlChargeParameter": dcEvtCtrlChargeParameter,
       "dcEvtCtrlChargeVoltage": dcEvtCtrlChargeVoltage,
       "dcEvtCtrlChargeTempCompEnabled": dcEvtCtrlChargeTempCompEnabled,
       "dcEvtCtrlChargeMaxIBatt": dcEvtCtrlChargeMaxIBatt,
       "dcTempComp": dcTempComp,
       "dcTempCompType": dcTempCompType,
       "dcSlope": dcSlope,
       "dcStartTemp": dcStartTemp,
       "dcStopTemp": dcStopTemp,
       "dcMaxVoltage": dcMaxVoltage,
       "dcLowStopVoltage": dcLowStopVoltage,
       "dcLowStartTemp": dcLowStartTemp,
       "dcLowTempSlope": dcLowTempSlope,
       "dcHighStartTemp": dcHighStartTemp,
       "dcHighTempSlope": dcHighTempSlope,
       "dcHighStopVoltage": dcHighStopVoltage,
       "dcRunawayTemp": dcRunawayTemp,
       "dcRunawayVoltage": dcRunawayVoltage,
       "dcTempSupervision": dcTempSupervision,
       "dcHighTemp": dcHighTemp,
       "dcHighTempHyst": dcHighTempHyst,
       "dcInputOutput": dcInputOutput,
       "dcControlEventTable": dcControlEventTable,
       "dcControlEventEntry": dcControlEventEntry,
       "dcControlEventIndex": dcControlEventIndex,
       "dcControlEventName": dcControlEventName,
       "dcControlEventIdentifier": dcControlEventIdentifier,
       "dcControlEventValue": dcControlEventValue,
       "dcMisc": dcMisc,
       "dcTrapDestinationTable": dcTrapDestinationTable,
       "dcTrapDestinationEntry": dcTrapDestinationEntry,
       "dcTrapDestinationIndex": dcTrapDestinationIndex,
       "dcTrapDestinationIp": dcTrapDestinationIp,
       "dcTrapDestinationPort": dcTrapDestinationPort,
       "dcFileProcessingStatus": dcFileProcessingStatus,
       "dcResendActiveAlarmTraps": dcResendActiveAlarmTraps,
       "dcConfig": dcConfig,
       "dcDefaultLogEventTable": dcDefaultLogEventTable,
       "dcDefaultLogEventEntry": dcDefaultLogEventEntry,
       "dcDefaultLogEventIndex": dcDefaultLogEventIndex,
       "dcDefaultLogEventName": dcDefaultLogEventName,
       "dcDefaultLogEventLogged": dcDefaultLogEventLogged,
       "dcEventProcessingEventTable": dcEventProcessingEventTable,
       "dcEventProcessingEventEntry": dcEventProcessingEventEntry,
       "dcEventProcessingEventIndex": dcEventProcessingEventIndex,
       "dcEventProcessingEventName": dcEventProcessingEventName,
       "dcEventProcessingEventAssigned": dcEventProcessingEventAssigned,
       "dcEventProcessingEventType": dcEventProcessingEventType,
       "dcEventProcessingEventSelected": dcEventProcessingEventSelected,
       "dcLvdTable": dcLvdTable,
       "dcLvdEntry": dcLvdEntry,
       "dcLvdIndex": dcLvdIndex,
       "dcLvdName": dcLvdName,
       "dcLvdDisconnectDelay": dcLvdDisconnectDelay,
       "dcMeasurement": dcMeasurement,
       "dcMeasurementTable": dcMeasurementTable,
       "dcMeasurementEntry": dcMeasurementEntry,
       "dcMeasurementIndex": dcMeasurementIndex,
       "dcMeasurementName": dcMeasurementName,
       "dcMeasurementValue": dcMeasurementValue,
       "dcMeasurementScaleFactor": dcMeasurementScaleFactor,
       "dcMeasurementUnit": dcMeasurementUnit,
       "dcMeterPanel": dcMeterPanel,
       "dcMeterPanelEventTable": dcMeterPanelEventTable,
       "dcMeterPanelEventEntry": dcMeterPanelEventEntry,
       "dcMeterPanelEventIndex": dcMeterPanelEventIndex,
       "dcMeterPanelEventName": dcMeterPanelEventName,
       "dcMeterPanelEventValue": dcMeterPanelEventValue,
       "dcMeterPanelEventHourMeterValue": dcMeterPanelEventHourMeterValue,
       "controllerEvents": controllerEvents,
       "controllerEventObjects": controllerEventObjects,
       "controllerEventsV2": controllerEventsV2,
       "systemNonUrgentAlarm": systemNonUrgentAlarm,
       "systemUrgentAlarm": systemUrgentAlarm,
       "systemCriticalAlarm": systemCriticalAlarm}
)
