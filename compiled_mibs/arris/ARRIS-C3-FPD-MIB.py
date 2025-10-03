# SNMP MIB module (ARRIS-C3-FPD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\arris\ARRIS-C3-FPD-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:18:02 2025
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

(cmtsC3,) = mibBuilder.importSymbols(
    "ARRIS-MIB",
    "cmtsC3")

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

cmtsC3FPDMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 3)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DcxFPDObjects_ObjectIdentity = ObjectIdentity
dcxFPDObjects = _DcxFPDObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 3, 1)
)
_DcxFPDMsgTable_Object = MibTable
dcxFPDMsgTable = _DcxFPDMsgTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 3, 1, 1)
)
if mibBuilder.loadTexts:
    dcxFPDMsgTable.setStatus("current")
_DcxFPDMsgEntry_Object = MibTableRow
dcxFPDMsgEntry = _DcxFPDMsgEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 3, 1, 1, 1)
)
dcxFPDMsgEntry.setIndexNames(
    (0, "ARRIS-C3-FPD-MIB", "dcxFPDMsgIndex"),
)
if mibBuilder.loadTexts:
    dcxFPDMsgEntry.setStatus("current")
_DcxFPDMsgIndex_Type = Unsigned32
_DcxFPDMsgIndex_Object = MibTableColumn
dcxFPDMsgIndex = _DcxFPDMsgIndex_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 3, 1, 1, 1, 1),
    _DcxFPDMsgIndex_Type()
)
dcxFPDMsgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dcxFPDMsgIndex.setStatus("current")


class _DcxFPDMsgString_Type(OctetString):
    """Custom type dcxFPDMsgString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_DcxFPDMsgString_Type.__name__ = "OctetString"
_DcxFPDMsgString_Object = MibTableColumn
dcxFPDMsgString = _DcxFPDMsgString_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 3, 1, 1, 1, 2),
    _DcxFPDMsgString_Type()
)
dcxFPDMsgString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcxFPDMsgString.setStatus("current")
_DcxFPDControlGroup_ObjectIdentity = ObjectIdentity
dcxFPDControlGroup = _DcxFPDControlGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 3, 1, 2)
)


class _DcxFPDAttachedStatus_Type(Integer32):
    """Custom type dcxFPDAttachedStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("attached", 1),
          ("detached", 2))
    )


_DcxFPDAttachedStatus_Type.__name__ = "Integer32"
_DcxFPDAttachedStatus_Object = MibScalar
dcxFPDAttachedStatus = _DcxFPDAttachedStatus_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 3, 1, 2, 1),
    _DcxFPDAttachedStatus_Type()
)
dcxFPDAttachedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcxFPDAttachedStatus.setStatus("current")


class _DcxFPDPowerStatus1_Type(Integer32):
    """Custom type dcxFPDPowerStatus1 based on Integer32"""
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


_DcxFPDPowerStatus1_Type.__name__ = "Integer32"
_DcxFPDPowerStatus1_Object = MibScalar
dcxFPDPowerStatus1 = _DcxFPDPowerStatus1_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 3, 1, 2, 2),
    _DcxFPDPowerStatus1_Type()
)
dcxFPDPowerStatus1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcxFPDPowerStatus1.setStatus("current")


class _DcxFPDPowerStatus2_Type(Integer32):
    """Custom type dcxFPDPowerStatus2 based on Integer32"""
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


_DcxFPDPowerStatus2_Type.__name__ = "Integer32"
_DcxFPDPowerStatus2_Object = MibScalar
dcxFPDPowerStatus2 = _DcxFPDPowerStatus2_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 3, 1, 2, 3),
    _DcxFPDPowerStatus2_Type()
)
dcxFPDPowerStatus2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcxFPDPowerStatus2.setStatus("current")
_DcxFPDTemp1Status_Type = Integer32
_DcxFPDTemp1Status_Object = MibScalar
dcxFPDTemp1Status = _DcxFPDTemp1Status_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 3, 1, 2, 4),
    _DcxFPDTemp1Status_Type()
)
dcxFPDTemp1Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcxFPDTemp1Status.setStatus("current")
_DcxFPDTemp2Status_Type = Integer32
_DcxFPDTemp2Status_Object = MibScalar
dcxFPDTemp2Status = _DcxFPDTemp2Status_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 3, 1, 2, 5),
    _DcxFPDTemp2Status_Type()
)
dcxFPDTemp2Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcxFPDTemp2Status.setStatus("current")
_DcxFPDTemp3Status_Type = Integer32
_DcxFPDTemp3Status_Object = MibScalar
dcxFPDTemp3Status = _DcxFPDTemp3Status_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 3, 1, 2, 6),
    _DcxFPDTemp3Status_Type()
)
dcxFPDTemp3Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcxFPDTemp3Status.setStatus("current")
_DcxFPDTemp4Status_Type = Integer32
_DcxFPDTemp4Status_Object = MibScalar
dcxFPDTemp4Status = _DcxFPDTemp4Status_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 3, 1, 2, 7),
    _DcxFPDTemp4Status_Type()
)
dcxFPDTemp4Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcxFPDTemp4Status.setStatus("current")


class _DcxFPDFan1Status_Type(Integer32):
    """Custom type dcxFPDFan1Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rotating", 1),
          ("badRotating", 2))
    )


_DcxFPDFan1Status_Type.__name__ = "Integer32"
_DcxFPDFan1Status_Object = MibScalar
dcxFPDFan1Status = _DcxFPDFan1Status_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 3, 1, 2, 8),
    _DcxFPDFan1Status_Type()
)
dcxFPDFan1Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcxFPDFan1Status.setStatus("current")


class _DcxFPDFan2Status_Type(Integer32):
    """Custom type dcxFPDFan2Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rotating", 1),
          ("badRotating", 2))
    )


_DcxFPDFan2Status_Type.__name__ = "Integer32"
_DcxFPDFan2Status_Object = MibScalar
dcxFPDFan2Status = _DcxFPDFan2Status_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 3, 1, 2, 9),
    _DcxFPDFan2Status_Type()
)
dcxFPDFan2Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcxFPDFan2Status.setStatus("current")


class _DcxFPDFan3Status_Type(Integer32):
    """Custom type dcxFPDFan3Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rotating", 1),
          ("badRotating", 2))
    )


_DcxFPDFan3Status_Type.__name__ = "Integer32"
_DcxFPDFan3Status_Object = MibScalar
dcxFPDFan3Status = _DcxFPDFan3Status_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 3, 1, 2, 10),
    _DcxFPDFan3Status_Type()
)
dcxFPDFan3Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcxFPDFan3Status.setStatus("current")


class _DcxFPDFan4Status_Type(Integer32):
    """Custom type dcxFPDFan4Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rotating", 1),
          ("badRotating", 2))
    )


_DcxFPDFan4Status_Type.__name__ = "Integer32"
_DcxFPDFan4Status_Object = MibScalar
dcxFPDFan4Status = _DcxFPDFan4Status_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 3, 1, 2, 11),
    _DcxFPDFan4Status_Type()
)
dcxFPDFan4Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcxFPDFan4Status.setStatus("current")


class _DcxFPDFan5Status_Type(Integer32):
    """Custom type dcxFPDFan5Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rotating", 1),
          ("badRotating", 2))
    )


_DcxFPDFan5Status_Type.__name__ = "Integer32"
_DcxFPDFan5Status_Object = MibScalar
dcxFPDFan5Status = _DcxFPDFan5Status_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 3, 1, 2, 12),
    _DcxFPDFan5Status_Type()
)
dcxFPDFan5Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcxFPDFan5Status.setStatus("current")


class _DcxFPDFan6Status_Type(Integer32):
    """Custom type dcxFPDFan6Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rotating", 1),
          ("badRotating", 2))
    )


_DcxFPDFan6Status_Type.__name__ = "Integer32"
_DcxFPDFan6Status_Object = MibScalar
dcxFPDFan6Status = _DcxFPDFan6Status_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 3, 1, 2, 13),
    _DcxFPDFan6Status_Type()
)
dcxFPDFan6Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcxFPDFan6Status.setStatus("current")


class _DcxFPDFanUpperLimit_Type(Integer32):
    """Custom type dcxFPDFanUpperLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DcxFPDFanUpperLimit_Type.__name__ = "Integer32"
_DcxFPDFanUpperLimit_Object = MibScalar
dcxFPDFanUpperLimit = _DcxFPDFanUpperLimit_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 3, 1, 2, 14),
    _DcxFPDFanUpperLimit_Type()
)
dcxFPDFanUpperLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcxFPDFanUpperLimit.setStatus("current")


class _DcxFPDFanLowerLimit_Type(Integer32):
    """Custom type dcxFPDFanLowerLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DcxFPDFanLowerLimit_Type.__name__ = "Integer32"
_DcxFPDFanLowerLimit_Object = MibScalar
dcxFPDFanLowerLimit = _DcxFPDFanLowerLimit_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 3, 1, 2, 15),
    _DcxFPDFanLowerLimit_Type()
)
dcxFPDFanLowerLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcxFPDFanLowerLimit.setStatus("current")


class _DcxFPDLCDContrast_Type(Integer32):
    """Custom type dcxFPDLCDContrast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DcxFPDLCDContrast_Type.__name__ = "Integer32"
_DcxFPDLCDContrast_Object = MibScalar
dcxFPDLCDContrast = _DcxFPDLCDContrast_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 3, 1, 2, 16),
    _DcxFPDLCDContrast_Type()
)
dcxFPDLCDContrast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcxFPDLCDContrast.setStatus("current")


class _DcxFPDLedSetStatus_Type(Integer32):
    """Custom type dcxFPDLedSetStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DcxFPDLedSetStatus_Type.__name__ = "Integer32"
_DcxFPDLedSetStatus_Object = MibScalar
dcxFPDLedSetStatus = _DcxFPDLedSetStatus_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 3, 1, 2, 17),
    _DcxFPDLedSetStatus_Type()
)
dcxFPDLedSetStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcxFPDLedSetStatus.setStatus("current")
_DcxFPDHwRevision_Type = Integer32
_DcxFPDHwRevision_Object = MibScalar
dcxFPDHwRevision = _DcxFPDHwRevision_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 3, 1, 2, 18),
    _DcxFPDHwRevision_Type()
)
dcxFPDHwRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcxFPDHwRevision.setStatus("current")
_DcxFPDSwRevision_Type = Integer32
_DcxFPDSwRevision_Object = MibScalar
dcxFPDSwRevision = _DcxFPDSwRevision_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 3, 1, 2, 19),
    _DcxFPDSwRevision_Type()
)
dcxFPDSwRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcxFPDSwRevision.setStatus("current")
_DcxFPDTrapGroup_ObjectIdentity = ObjectIdentity
dcxFPDTrapGroup = _DcxFPDTrapGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 3, 1, 3)
)
_DcxFPDConformance_ObjectIdentity = ObjectIdentity
dcxFPDConformance = _DcxFPDConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 3, 1, 4)
)
_DcxFPDCompliances_ObjectIdentity = ObjectIdentity
dcxFPDCompliances = _DcxFPDCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 3, 1, 4, 1)
)
_DcxFPDGroups_ObjectIdentity = ObjectIdentity
dcxFPDGroups = _DcxFPDGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 3, 1, 4, 2)
)

# Managed Objects groups

dcxFPDMsgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 3, 1, 4, 2, 1)
)
dcxFPDMsgGroup.setObjects(
    ("ARRIS-C3-FPD-MIB", "dcxFPDMsgString")
)
if mibBuilder.loadTexts:
    dcxFPDMsgGroup.setStatus("current")

dcxFPDControlConfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 3, 1, 4, 2, 2)
)
dcxFPDControlConfGroup.setObjects(
      *(("ARRIS-C3-FPD-MIB", "dcxFPDAttachedStatus"),
        ("ARRIS-C3-FPD-MIB", "dcxFPDPowerStatus1"),
        ("ARRIS-C3-FPD-MIB", "dcxFPDPowerStatus2"),
        ("ARRIS-C3-FPD-MIB", "dcxFPDTemp1Status"),
        ("ARRIS-C3-FPD-MIB", "dcxFPDTemp2Status"),
        ("ARRIS-C3-FPD-MIB", "dcxFPDTemp3Status"),
        ("ARRIS-C3-FPD-MIB", "dcxFPDTemp4Status"),
        ("ARRIS-C3-FPD-MIB", "dcxFPDFan1Status"),
        ("ARRIS-C3-FPD-MIB", "dcxFPDFan2Status"),
        ("ARRIS-C3-FPD-MIB", "dcxFPDFan3Status"),
        ("ARRIS-C3-FPD-MIB", "dcxFPDFan4Status"),
        ("ARRIS-C3-FPD-MIB", "dcxFPDFan5Status"),
        ("ARRIS-C3-FPD-MIB", "dcxFPDFan6Status"),
        ("ARRIS-C3-FPD-MIB", "dcxFPDFanUpperLimit"),
        ("ARRIS-C3-FPD-MIB", "dcxFPDFanLowerLimit"),
        ("ARRIS-C3-FPD-MIB", "dcxFPDLCDContrast"),
        ("ARRIS-C3-FPD-MIB", "dcxFPDLedSetStatus"),
        ("ARRIS-C3-FPD-MIB", "dcxFPDHwRevision"),
        ("ARRIS-C3-FPD-MIB", "dcxFPDSwRevision"))
)
if mibBuilder.loadTexts:
    dcxFPDControlConfGroup.setStatus("current")


# Notification objects

dcxFPDAttached = NotificationType(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 3, 1, 3, 1)
)
if mibBuilder.loadTexts:
    dcxFPDAttached.setStatus(
        "current"
    )

dcxFPDDetached = NotificationType(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 3, 1, 3, 2)
)
if mibBuilder.loadTexts:
    dcxFPDDetached.setStatus(
        "current"
    )

dcxFPDFan1Fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 3, 1, 3, 3)
)
if mibBuilder.loadTexts:
    dcxFPDFan1Fail.setStatus(
        "current"
    )

dcxFPDFan1FailClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 3, 1, 3, 4)
)
if mibBuilder.loadTexts:
    dcxFPDFan1FailClr.setStatus(
        "current"
    )

dcxFPDFan2Fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 3, 1, 3, 5)
)
if mibBuilder.loadTexts:
    dcxFPDFan2Fail.setStatus(
        "current"
    )

dcxFPDFan2FailClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 3, 1, 3, 6)
)
if mibBuilder.loadTexts:
    dcxFPDFan2FailClr.setStatus(
        "current"
    )

dcxFPDFan3Fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 3, 1, 3, 7)
)
if mibBuilder.loadTexts:
    dcxFPDFan3Fail.setStatus(
        "current"
    )

dcxFPDFan3FailClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 3, 1, 3, 8)
)
if mibBuilder.loadTexts:
    dcxFPDFan3FailClr.setStatus(
        "current"
    )

dcxFPDFan4Fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 3, 1, 3, 9)
)
if mibBuilder.loadTexts:
    dcxFPDFan4Fail.setStatus(
        "current"
    )

dcxFPDFan4FailClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 3, 1, 3, 10)
)
if mibBuilder.loadTexts:
    dcxFPDFan4FailClr.setStatus(
        "current"
    )

dcxFPDFan5Fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 3, 1, 3, 11)
)
if mibBuilder.loadTexts:
    dcxFPDFan5Fail.setStatus(
        "current"
    )

dcxFPDFan5FailClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 3, 1, 3, 12)
)
if mibBuilder.loadTexts:
    dcxFPDFan5FailClr.setStatus(
        "current"
    )

dcxFPDFan6Fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 3, 1, 3, 13)
)
if mibBuilder.loadTexts:
    dcxFPDFan6Fail.setStatus(
        "current"
    )

dcxFPDFan6FailClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 3, 1, 3, 14)
)
if mibBuilder.loadTexts:
    dcxFPDFan6FailClr.setStatus(
        "current"
    )

dcxFPDPwr1Fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 3, 1, 3, 15)
)
if mibBuilder.loadTexts:
    dcxFPDPwr1Fail.setStatus(
        "current"
    )

dcxFPDPwr1FailClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 3, 1, 3, 16)
)
if mibBuilder.loadTexts:
    dcxFPDPwr1FailClr.setStatus(
        "current"
    )

dcxFPDPwr2Fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 3, 1, 3, 17)
)
if mibBuilder.loadTexts:
    dcxFPDPwr2Fail.setStatus(
        "current"
    )

dcxFPDPwr2FailClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 3, 1, 3, 18)
)
if mibBuilder.loadTexts:
    dcxFPDPwr2FailClr.setStatus(
        "current"
    )

dcxFPDTempOkay = NotificationType(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 3, 1, 3, 19)
)
if mibBuilder.loadTexts:
    dcxFPDTempOkay.setStatus(
        "current"
    )

dcxFPDTempBad = NotificationType(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 3, 1, 3, 20)
)
if mibBuilder.loadTexts:
    dcxFPDTempBad.setStatus(
        "current"
    )

dcxFPDTempCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 3, 1, 3, 21)
)
if mibBuilder.loadTexts:
    dcxFPDTempCritical.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

dcxFPDCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 3, 1, 4, 1, 1)
)
dcxFPDCompliance.setObjects(
      *(("ARRIS-C3-FPD-MIB", "dcxFPDMsgGroup"),
        ("ARRIS-C3-FPD-MIB", "dcxFPDControlConfGroup"))
)
if mibBuilder.loadTexts:
    dcxFPDCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARRIS-C3-FPD-MIB",
    **{"cmtsC3FPDMIB": cmtsC3FPDMIB,
       "dcxFPDObjects": dcxFPDObjects,
       "dcxFPDMsgTable": dcxFPDMsgTable,
       "dcxFPDMsgEntry": dcxFPDMsgEntry,
       "dcxFPDMsgIndex": dcxFPDMsgIndex,
       "dcxFPDMsgString": dcxFPDMsgString,
       "dcxFPDControlGroup": dcxFPDControlGroup,
       "dcxFPDAttachedStatus": dcxFPDAttachedStatus,
       "dcxFPDPowerStatus1": dcxFPDPowerStatus1,
       "dcxFPDPowerStatus2": dcxFPDPowerStatus2,
       "dcxFPDTemp1Status": dcxFPDTemp1Status,
       "dcxFPDTemp2Status": dcxFPDTemp2Status,
       "dcxFPDTemp3Status": dcxFPDTemp3Status,
       "dcxFPDTemp4Status": dcxFPDTemp4Status,
       "dcxFPDFan1Status": dcxFPDFan1Status,
       "dcxFPDFan2Status": dcxFPDFan2Status,
       "dcxFPDFan3Status": dcxFPDFan3Status,
       "dcxFPDFan4Status": dcxFPDFan4Status,
       "dcxFPDFan5Status": dcxFPDFan5Status,
       "dcxFPDFan6Status": dcxFPDFan6Status,
       "dcxFPDFanUpperLimit": dcxFPDFanUpperLimit,
       "dcxFPDFanLowerLimit": dcxFPDFanLowerLimit,
       "dcxFPDLCDContrast": dcxFPDLCDContrast,
       "dcxFPDLedSetStatus": dcxFPDLedSetStatus,
       "dcxFPDHwRevision": dcxFPDHwRevision,
       "dcxFPDSwRevision": dcxFPDSwRevision,
       "dcxFPDTrapGroup": dcxFPDTrapGroup,
       "dcxFPDAttached": dcxFPDAttached,
       "dcxFPDDetached": dcxFPDDetached,
       "dcxFPDFan1Fail": dcxFPDFan1Fail,
       "dcxFPDFan1FailClr": dcxFPDFan1FailClr,
       "dcxFPDFan2Fail": dcxFPDFan2Fail,
       "dcxFPDFan2FailClr": dcxFPDFan2FailClr,
       "dcxFPDFan3Fail": dcxFPDFan3Fail,
       "dcxFPDFan3FailClr": dcxFPDFan3FailClr,
       "dcxFPDFan4Fail": dcxFPDFan4Fail,
       "dcxFPDFan4FailClr": dcxFPDFan4FailClr,
       "dcxFPDFan5Fail": dcxFPDFan5Fail,
       "dcxFPDFan5FailClr": dcxFPDFan5FailClr,
       "dcxFPDFan6Fail": dcxFPDFan6Fail,
       "dcxFPDFan6FailClr": dcxFPDFan6FailClr,
       "dcxFPDPwr1Fail": dcxFPDPwr1Fail,
       "dcxFPDPwr1FailClr": dcxFPDPwr1FailClr,
       "dcxFPDPwr2Fail": dcxFPDPwr2Fail,
       "dcxFPDPwr2FailClr": dcxFPDPwr2FailClr,
       "dcxFPDTempOkay": dcxFPDTempOkay,
       "dcxFPDTempBad": dcxFPDTempBad,
       "dcxFPDTempCritical": dcxFPDTempCritical,
       "dcxFPDConformance": dcxFPDConformance,
       "dcxFPDCompliances": dcxFPDCompliances,
       "dcxFPDCompliance": dcxFPDCompliance,
       "dcxFPDGroups": dcxFPDGroups,
       "dcxFPDMsgGroup": dcxFPDMsgGroup,
       "dcxFPDControlConfGroup": dcxFPDControlConfGroup}
)
