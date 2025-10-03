# SNMP MIB module (HH3C-MIRRORGROUP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\comware\HH3C-MIRRORGROUP-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:32:11 2025
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

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

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
    "iso")

(DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

hh3cMirrGroup = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 68)
)
if mibBuilder.loadTexts:
    hh3cMirrGroup.setRevisions(
        ("2006-01-10 19:03",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cMGInfoObjects_ObjectIdentity = ObjectIdentity
hh3cMGInfoObjects = _Hh3cMGInfoObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 68, 1)
)
_Hh3cMGObjects_ObjectIdentity = ObjectIdentity
hh3cMGObjects = _Hh3cMGObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 68, 1, 1)
)
_Hh3cMGTable_Object = MibTable
hh3cMGTable = _Hh3cMGTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 68, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cMGTable.setStatus("current")
_Hh3cMGEntry_Object = MibTableRow
hh3cMGEntry = _Hh3cMGEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 68, 1, 1, 1, 1)
)
hh3cMGEntry.setIndexNames(
    (0, "HH3C-MIRRORGROUP-MIB", "hh3cMGID"),
)
if mibBuilder.loadTexts:
    hh3cMGEntry.setStatus("current")


class _Hh3cMGID_Type(Integer32):
    """Custom type hh3cMGID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hh3cMGID_Type.__name__ = "Integer32"
_Hh3cMGID_Object = MibTableColumn
hh3cMGID = _Hh3cMGID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 68, 1, 1, 1, 1, 1),
    _Hh3cMGID_Type()
)
hh3cMGID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cMGID.setStatus("current")


class _Hh3cMGType_Type(Integer32):
    """Custom type hh3cMGType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("remoteSource", 2),
          ("remoteDestination", 3))
    )


_Hh3cMGType_Type.__name__ = "Integer32"
_Hh3cMGType_Object = MibTableColumn
hh3cMGType = _Hh3cMGType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 68, 1, 1, 1, 1, 2),
    _Hh3cMGType_Type()
)
hh3cMGType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMGType.setStatus("current")


class _Hh3cMGStatus_Type(Integer32):
    """Custom type hh3cMGStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_Hh3cMGStatus_Type.__name__ = "Integer32"
_Hh3cMGStatus_Object = MibTableColumn
hh3cMGStatus = _Hh3cMGStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 68, 1, 1, 1, 1, 3),
    _Hh3cMGStatus_Type()
)
hh3cMGStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMGStatus.setStatus("current")
_Hh3cMGRowStatus_Type = RowStatus
_Hh3cMGRowStatus_Object = MibTableColumn
hh3cMGRowStatus = _Hh3cMGRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 68, 1, 1, 1, 1, 4),
    _Hh3cMGRowStatus_Type()
)
hh3cMGRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMGRowStatus.setStatus("current")
_Hh3cMGMirrorIfObjects_ObjectIdentity = ObjectIdentity
hh3cMGMirrorIfObjects = _Hh3cMGMirrorIfObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 68, 1, 2)
)
_Hh3cMGMirrorIfTable_Object = MibTable
hh3cMGMirrorIfTable = _Hh3cMGMirrorIfTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 68, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hh3cMGMirrorIfTable.setStatus("current")
_Hh3cMGMirrorIfEntry_Object = MibTableRow
hh3cMGMirrorIfEntry = _Hh3cMGMirrorIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 68, 1, 2, 1, 1)
)
hh3cMGMirrorIfEntry.setIndexNames(
    (0, "HH3C-MIRRORGROUP-MIB", "hh3cMGID"),
    (0, "HH3C-MIRRORGROUP-MIB", "hh3cMGMirrorIfIndex"),
    (0, "HH3C-MIRRORGROUP-MIB", "hh3cMGMirrorDirection"),
)
if mibBuilder.loadTexts:
    hh3cMGMirrorIfEntry.setStatus("current")
_Hh3cMGMirrorIfIndex_Type = Integer32
_Hh3cMGMirrorIfIndex_Object = MibTableColumn
hh3cMGMirrorIfIndex = _Hh3cMGMirrorIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 68, 1, 2, 1, 1, 1),
    _Hh3cMGMirrorIfIndex_Type()
)
hh3cMGMirrorIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cMGMirrorIfIndex.setStatus("current")


class _Hh3cMGMirrorDirection_Type(Integer32):
    """Custom type hh3cMGMirrorDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inbound", 1),
          ("outbound", 2),
          ("both", 3))
    )


_Hh3cMGMirrorDirection_Type.__name__ = "Integer32"
_Hh3cMGMirrorDirection_Object = MibTableColumn
hh3cMGMirrorDirection = _Hh3cMGMirrorDirection_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 68, 1, 2, 1, 1, 2),
    _Hh3cMGMirrorDirection_Type()
)
hh3cMGMirrorDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cMGMirrorDirection.setStatus("current")
_Hh3cMGMirrorRowStatus_Type = RowStatus
_Hh3cMGMirrorRowStatus_Object = MibTableColumn
hh3cMGMirrorRowStatus = _Hh3cMGMirrorRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 68, 1, 2, 1, 1, 3),
    _Hh3cMGMirrorRowStatus_Type()
)
hh3cMGMirrorRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMGMirrorRowStatus.setStatus("current")
_Hh3cMGMonitorIfObjects_ObjectIdentity = ObjectIdentity
hh3cMGMonitorIfObjects = _Hh3cMGMonitorIfObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 68, 1, 3)
)
_Hh3cMGMonitorIfTable_Object = MibTable
hh3cMGMonitorIfTable = _Hh3cMGMonitorIfTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 68, 1, 3, 1)
)
if mibBuilder.loadTexts:
    hh3cMGMonitorIfTable.setStatus("current")
_Hh3cMGMonitorIfEntry_Object = MibTableRow
hh3cMGMonitorIfEntry = _Hh3cMGMonitorIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 68, 1, 3, 1, 1)
)
hh3cMGMonitorIfEntry.setIndexNames(
    (0, "HH3C-MIRRORGROUP-MIB", "hh3cMGID"),
    (0, "HH3C-MIRRORGROUP-MIB", "hh3cMGMonitorIfIndex"),
)
if mibBuilder.loadTexts:
    hh3cMGMonitorIfEntry.setStatus("current")
_Hh3cMGMonitorIfIndex_Type = Integer32
_Hh3cMGMonitorIfIndex_Object = MibTableColumn
hh3cMGMonitorIfIndex = _Hh3cMGMonitorIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 68, 1, 3, 1, 1, 1),
    _Hh3cMGMonitorIfIndex_Type()
)
hh3cMGMonitorIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cMGMonitorIfIndex.setStatus("current")
_Hh3cMGMonitorRowStatus_Type = RowStatus
_Hh3cMGMonitorRowStatus_Object = MibTableColumn
hh3cMGMonitorRowStatus = _Hh3cMGMonitorRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 68, 1, 3, 1, 1, 2),
    _Hh3cMGMonitorRowStatus_Type()
)
hh3cMGMonitorRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMGMonitorRowStatus.setStatus("current")
_Hh3cMGReflectorIfObjects_ObjectIdentity = ObjectIdentity
hh3cMGReflectorIfObjects = _Hh3cMGReflectorIfObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 68, 1, 4)
)
_Hh3cMGReflectorIfTable_Object = MibTable
hh3cMGReflectorIfTable = _Hh3cMGReflectorIfTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 68, 1, 4, 1)
)
if mibBuilder.loadTexts:
    hh3cMGReflectorIfTable.setStatus("current")
_Hh3cMGReflectorIfEntry_Object = MibTableRow
hh3cMGReflectorIfEntry = _Hh3cMGReflectorIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 68, 1, 4, 1, 1)
)
hh3cMGReflectorIfEntry.setIndexNames(
    (0, "HH3C-MIRRORGROUP-MIB", "hh3cMGID"),
    (0, "HH3C-MIRRORGROUP-MIB", "hh3cMGReflectorIfIndex"),
)
if mibBuilder.loadTexts:
    hh3cMGReflectorIfEntry.setStatus("current")
_Hh3cMGReflectorIfIndex_Type = Integer32
_Hh3cMGReflectorIfIndex_Object = MibTableColumn
hh3cMGReflectorIfIndex = _Hh3cMGReflectorIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 68, 1, 4, 1, 1, 1),
    _Hh3cMGReflectorIfIndex_Type()
)
hh3cMGReflectorIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cMGReflectorIfIndex.setStatus("current")
_Hh3cMGReflectorRowStatus_Type = RowStatus
_Hh3cMGReflectorRowStatus_Object = MibTableColumn
hh3cMGReflectorRowStatus = _Hh3cMGReflectorRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 68, 1, 4, 1, 1, 2),
    _Hh3cMGReflectorRowStatus_Type()
)
hh3cMGReflectorRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMGReflectorRowStatus.setStatus("current")
_Hh3cMGRprobeVlanObjects_ObjectIdentity = ObjectIdentity
hh3cMGRprobeVlanObjects = _Hh3cMGRprobeVlanObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 68, 1, 5)
)
_Hh3cMGRprobeVlanTable_Object = MibTable
hh3cMGRprobeVlanTable = _Hh3cMGRprobeVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 68, 1, 5, 1)
)
if mibBuilder.loadTexts:
    hh3cMGRprobeVlanTable.setStatus("current")
_Hh3cMGRprobeVlanEntry_Object = MibTableRow
hh3cMGRprobeVlanEntry = _Hh3cMGRprobeVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 68, 1, 5, 1, 1)
)
hh3cMGRprobeVlanEntry.setIndexNames(
    (0, "HH3C-MIRRORGROUP-MIB", "hh3cMGID"),
    (0, "HH3C-MIRRORGROUP-MIB", "hh3cMGRprobeVlanID"),
)
if mibBuilder.loadTexts:
    hh3cMGRprobeVlanEntry.setStatus("current")


class _Hh3cMGRprobeVlanID_Type(Integer32):
    """Custom type hh3cMGRprobeVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Hh3cMGRprobeVlanID_Type.__name__ = "Integer32"
_Hh3cMGRprobeVlanID_Object = MibTableColumn
hh3cMGRprobeVlanID = _Hh3cMGRprobeVlanID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 68, 1, 5, 1, 1, 1),
    _Hh3cMGRprobeVlanID_Type()
)
hh3cMGRprobeVlanID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cMGRprobeVlanID.setStatus("current")
_Hh3cMGRprobeVlanRowStatus_Type = RowStatus
_Hh3cMGRprobeVlanRowStatus_Object = MibTableColumn
hh3cMGRprobeVlanRowStatus = _Hh3cMGRprobeVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 68, 1, 5, 1, 1, 2),
    _Hh3cMGRprobeVlanRowStatus_Type()
)
hh3cMGRprobeVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMGRprobeVlanRowStatus.setStatus("current")
_Hh3cMGEgressIfObjects_ObjectIdentity = ObjectIdentity
hh3cMGEgressIfObjects = _Hh3cMGEgressIfObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 68, 1, 6)
)
_Hh3cMGEgressIfTable_Object = MibTable
hh3cMGEgressIfTable = _Hh3cMGEgressIfTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 68, 1, 6, 1)
)
if mibBuilder.loadTexts:
    hh3cMGEgressIfTable.setStatus("current")
_Hh3cMGEgressIfEntry_Object = MibTableRow
hh3cMGEgressIfEntry = _Hh3cMGEgressIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 68, 1, 6, 1, 1)
)
hh3cMGEgressIfEntry.setIndexNames(
    (0, "HH3C-MIRRORGROUP-MIB", "hh3cMGID"),
    (0, "HH3C-MIRRORGROUP-MIB", "hh3cMGEgressIfIndex"),
)
if mibBuilder.loadTexts:
    hh3cMGEgressIfEntry.setStatus("current")


class _Hh3cMGEgressIfIndex_Type(Integer32):
    """Custom type hh3cMGEgressIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hh3cMGEgressIfIndex_Type.__name__ = "Integer32"
_Hh3cMGEgressIfIndex_Object = MibTableColumn
hh3cMGEgressIfIndex = _Hh3cMGEgressIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 68, 1, 6, 1, 1, 1),
    _Hh3cMGEgressIfIndex_Type()
)
hh3cMGEgressIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cMGEgressIfIndex.setStatus("current")
_Hh3cMGEgressRowStatus_Type = RowStatus
_Hh3cMGEgressRowStatus_Object = MibTableColumn
hh3cMGEgressRowStatus = _Hh3cMGEgressRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 68, 1, 6, 1, 1, 2),
    _Hh3cMGEgressRowStatus_Type()
)
hh3cMGEgressRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMGEgressRowStatus.setStatus("current")
_Hh3cMGMirrorVlanObjects_ObjectIdentity = ObjectIdentity
hh3cMGMirrorVlanObjects = _Hh3cMGMirrorVlanObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 68, 1, 7)
)
_Hh3cMGMirrorVlanTable_Object = MibTable
hh3cMGMirrorVlanTable = _Hh3cMGMirrorVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 68, 1, 7, 1)
)
if mibBuilder.loadTexts:
    hh3cMGMirrorVlanTable.setStatus("current")
_Hh3cMGMirrorVlanEntry_Object = MibTableRow
hh3cMGMirrorVlanEntry = _Hh3cMGMirrorVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 68, 1, 7, 1, 1)
)
hh3cMGMirrorVlanEntry.setIndexNames(
    (0, "HH3C-MIRRORGROUP-MIB", "hh3cMGID"),
    (0, "HH3C-MIRRORGROUP-MIB", "hh3cMGMirrorVlanID"),
)
if mibBuilder.loadTexts:
    hh3cMGMirrorVlanEntry.setStatus("current")


class _Hh3cMGMirrorVlanID_Type(Integer32):
    """Custom type hh3cMGMirrorVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Hh3cMGMirrorVlanID_Type.__name__ = "Integer32"
_Hh3cMGMirrorVlanID_Object = MibTableColumn
hh3cMGMirrorVlanID = _Hh3cMGMirrorVlanID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 68, 1, 7, 1, 1, 1),
    _Hh3cMGMirrorVlanID_Type()
)
hh3cMGMirrorVlanID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cMGMirrorVlanID.setStatus("current")


class _Hh3cMGMirrorVlanDirection_Type(Integer32):
    """Custom type hh3cMGMirrorVlanDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inbound", 1),
          ("outbound", 2),
          ("both", 3))
    )


_Hh3cMGMirrorVlanDirection_Type.__name__ = "Integer32"
_Hh3cMGMirrorVlanDirection_Object = MibTableColumn
hh3cMGMirrorVlanDirection = _Hh3cMGMirrorVlanDirection_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 68, 1, 7, 1, 1, 2),
    _Hh3cMGMirrorVlanDirection_Type()
)
hh3cMGMirrorVlanDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMGMirrorVlanDirection.setStatus("current")
_Hh3cMGMirrorVlanRowStatus_Type = RowStatus
_Hh3cMGMirrorVlanRowStatus_Object = MibTableColumn
hh3cMGMirrorVlanRowStatus = _Hh3cMGMirrorVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 68, 1, 7, 1, 1, 3),
    _Hh3cMGMirrorVlanRowStatus_Type()
)
hh3cMGMirrorVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMGMirrorVlanRowStatus.setStatus("current")
_Hh3cMGMirrorCpuObjects_ObjectIdentity = ObjectIdentity
hh3cMGMirrorCpuObjects = _Hh3cMGMirrorCpuObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 68, 1, 8)
)
_Hh3cMGMirrorCpuTable_Object = MibTable
hh3cMGMirrorCpuTable = _Hh3cMGMirrorCpuTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 68, 1, 8, 1)
)
if mibBuilder.loadTexts:
    hh3cMGMirrorCpuTable.setStatus("current")
_Hh3cMGMirrorCpuEntry_Object = MibTableRow
hh3cMGMirrorCpuEntry = _Hh3cMGMirrorCpuEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 68, 1, 8, 1, 1)
)
hh3cMGMirrorCpuEntry.setIndexNames(
    (0, "HH3C-MIRRORGROUP-MIB", "hh3cMGID"),
    (0, "HH3C-MIRRORGROUP-MIB", "hh3cMGMirrorCpuChassis"),
    (0, "HH3C-MIRRORGROUP-MIB", "hh3cMGMirrorCpuSlot"),
)
if mibBuilder.loadTexts:
    hh3cMGMirrorCpuEntry.setStatus("current")
_Hh3cMGMirrorCpuChassis_Type = Unsigned32
_Hh3cMGMirrorCpuChassis_Object = MibTableColumn
hh3cMGMirrorCpuChassis = _Hh3cMGMirrorCpuChassis_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 68, 1, 8, 1, 1, 1),
    _Hh3cMGMirrorCpuChassis_Type()
)
hh3cMGMirrorCpuChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cMGMirrorCpuChassis.setStatus("current")
_Hh3cMGMirrorCpuSlot_Type = Unsigned32
_Hh3cMGMirrorCpuSlot_Object = MibTableColumn
hh3cMGMirrorCpuSlot = _Hh3cMGMirrorCpuSlot_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 68, 1, 8, 1, 1, 2),
    _Hh3cMGMirrorCpuSlot_Type()
)
hh3cMGMirrorCpuSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cMGMirrorCpuSlot.setStatus("current")


class _Hh3cMGMirrorCpuDirection_Type(Integer32):
    """Custom type hh3cMGMirrorCpuDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inbound", 1),
          ("outbound", 2),
          ("both", 3))
    )


_Hh3cMGMirrorCpuDirection_Type.__name__ = "Integer32"
_Hh3cMGMirrorCpuDirection_Object = MibTableColumn
hh3cMGMirrorCpuDirection = _Hh3cMGMirrorCpuDirection_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 68, 1, 8, 1, 1, 3),
    _Hh3cMGMirrorCpuDirection_Type()
)
hh3cMGMirrorCpuDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMGMirrorCpuDirection.setStatus("current")
_Hh3cMGMirrorCpuRowStatus_Type = RowStatus
_Hh3cMGMirrorCpuRowStatus_Object = MibTableColumn
hh3cMGMirrorCpuRowStatus = _Hh3cMGMirrorCpuRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 68, 1, 8, 1, 1, 4),
    _Hh3cMGMirrorCpuRowStatus_Type()
)
hh3cMGMirrorCpuRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMGMirrorCpuRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-MIRRORGROUP-MIB",
    **{"hh3cMirrGroup": hh3cMirrGroup,
       "hh3cMGInfoObjects": hh3cMGInfoObjects,
       "hh3cMGObjects": hh3cMGObjects,
       "hh3cMGTable": hh3cMGTable,
       "hh3cMGEntry": hh3cMGEntry,
       "hh3cMGID": hh3cMGID,
       "hh3cMGType": hh3cMGType,
       "hh3cMGStatus": hh3cMGStatus,
       "hh3cMGRowStatus": hh3cMGRowStatus,
       "hh3cMGMirrorIfObjects": hh3cMGMirrorIfObjects,
       "hh3cMGMirrorIfTable": hh3cMGMirrorIfTable,
       "hh3cMGMirrorIfEntry": hh3cMGMirrorIfEntry,
       "hh3cMGMirrorIfIndex": hh3cMGMirrorIfIndex,
       "hh3cMGMirrorDirection": hh3cMGMirrorDirection,
       "hh3cMGMirrorRowStatus": hh3cMGMirrorRowStatus,
       "hh3cMGMonitorIfObjects": hh3cMGMonitorIfObjects,
       "hh3cMGMonitorIfTable": hh3cMGMonitorIfTable,
       "hh3cMGMonitorIfEntry": hh3cMGMonitorIfEntry,
       "hh3cMGMonitorIfIndex": hh3cMGMonitorIfIndex,
       "hh3cMGMonitorRowStatus": hh3cMGMonitorRowStatus,
       "hh3cMGReflectorIfObjects": hh3cMGReflectorIfObjects,
       "hh3cMGReflectorIfTable": hh3cMGReflectorIfTable,
       "hh3cMGReflectorIfEntry": hh3cMGReflectorIfEntry,
       "hh3cMGReflectorIfIndex": hh3cMGReflectorIfIndex,
       "hh3cMGReflectorRowStatus": hh3cMGReflectorRowStatus,
       "hh3cMGRprobeVlanObjects": hh3cMGRprobeVlanObjects,
       "hh3cMGRprobeVlanTable": hh3cMGRprobeVlanTable,
       "hh3cMGRprobeVlanEntry": hh3cMGRprobeVlanEntry,
       "hh3cMGRprobeVlanID": hh3cMGRprobeVlanID,
       "hh3cMGRprobeVlanRowStatus": hh3cMGRprobeVlanRowStatus,
       "hh3cMGEgressIfObjects": hh3cMGEgressIfObjects,
       "hh3cMGEgressIfTable": hh3cMGEgressIfTable,
       "hh3cMGEgressIfEntry": hh3cMGEgressIfEntry,
       "hh3cMGEgressIfIndex": hh3cMGEgressIfIndex,
       "hh3cMGEgressRowStatus": hh3cMGEgressRowStatus,
       "hh3cMGMirrorVlanObjects": hh3cMGMirrorVlanObjects,
       "hh3cMGMirrorVlanTable": hh3cMGMirrorVlanTable,
       "hh3cMGMirrorVlanEntry": hh3cMGMirrorVlanEntry,
       "hh3cMGMirrorVlanID": hh3cMGMirrorVlanID,
       "hh3cMGMirrorVlanDirection": hh3cMGMirrorVlanDirection,
       "hh3cMGMirrorVlanRowStatus": hh3cMGMirrorVlanRowStatus,
       "hh3cMGMirrorCpuObjects": hh3cMGMirrorCpuObjects,
       "hh3cMGMirrorCpuTable": hh3cMGMirrorCpuTable,
       "hh3cMGMirrorCpuEntry": hh3cMGMirrorCpuEntry,
       "hh3cMGMirrorCpuChassis": hh3cMGMirrorCpuChassis,
       "hh3cMGMirrorCpuSlot": hh3cMGMirrorCpuSlot,
       "hh3cMGMirrorCpuDirection": hh3cMGMirrorCpuDirection,
       "hh3cMGMirrorCpuRowStatus": hh3cMGMirrorCpuRowStatus}
)
