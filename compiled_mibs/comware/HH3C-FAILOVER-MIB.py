# SNMP MIB module (HH3C-FAILOVER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\comware\HH3C-FAILOVER-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:31:27 2025
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

hh3cFailover = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 164)
)
if mibBuilder.loadTexts:
    hh3cFailover.setRevisions(
        ("2015-10-27 10:40",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cFailoverScalarObjects_ObjectIdentity = ObjectIdentity
hh3cFailoverScalarObjects = _Hh3cFailoverScalarObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 164, 1)
)
_Hh3cFailoverMaxNum_Type = Unsigned32
_Hh3cFailoverMaxNum_Object = MibScalar
hh3cFailoverMaxNum = _Hh3cFailoverMaxNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 164, 1, 1),
    _Hh3cFailoverMaxNum_Type()
)
hh3cFailoverMaxNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFailoverMaxNum.setStatus("current")
_Hh3cFailoverCurrentNum_Type = Unsigned32
_Hh3cFailoverCurrentNum_Object = MibScalar
hh3cFailoverCurrentNum = _Hh3cFailoverCurrentNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 164, 1, 2),
    _Hh3cFailoverCurrentNum_Type()
)
hh3cFailoverCurrentNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFailoverCurrentNum.setStatus("current")
_Hh3cFailoverTables_ObjectIdentity = ObjectIdentity
hh3cFailoverTables = _Hh3cFailoverTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 164, 2)
)
_Hh3cFailoverCfgTable_Object = MibTable
hh3cFailoverCfgTable = _Hh3cFailoverCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 164, 2, 1)
)
if mibBuilder.loadTexts:
    hh3cFailoverCfgTable.setStatus("current")
_Hh3cFailoverCfgEntry_Object = MibTableRow
hh3cFailoverCfgEntry = _Hh3cFailoverCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 164, 2, 1, 1)
)
hh3cFailoverCfgEntry.setIndexNames(
    (0, "HH3C-FAILOVER-MIB", "hh3cFailoverIndex"),
)
if mibBuilder.loadTexts:
    hh3cFailoverCfgEntry.setStatus("current")


class _Hh3cFailoverIndex_Type(Unsigned32):
    """Custom type hh3cFailoverIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Hh3cFailoverIndex_Type.__name__ = "Unsigned32"
_Hh3cFailoverIndex_Object = MibTableColumn
hh3cFailoverIndex = _Hh3cFailoverIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 164, 2, 1, 1, 1),
    _Hh3cFailoverIndex_Type()
)
hh3cFailoverIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cFailoverIndex.setStatus("current")


class _Hh3cFailoverName_Type(DisplayString):
    """Custom type hh3cFailoverName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_Hh3cFailoverName_Type.__name__ = "DisplayString"
_Hh3cFailoverName_Object = MibTableColumn
hh3cFailoverName = _Hh3cFailoverName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 164, 2, 1, 1, 2),
    _Hh3cFailoverName_Type()
)
hh3cFailoverName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cFailoverName.setStatus("current")


class _Hh3cFailoverPrimaryChassisID_Type(Integer32):
    """Custom type hh3cFailoverPrimaryChassisID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 255),
    )


_Hh3cFailoverPrimaryChassisID_Type.__name__ = "Integer32"
_Hh3cFailoverPrimaryChassisID_Object = MibTableColumn
hh3cFailoverPrimaryChassisID = _Hh3cFailoverPrimaryChassisID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 164, 2, 1, 1, 3),
    _Hh3cFailoverPrimaryChassisID_Type()
)
hh3cFailoverPrimaryChassisID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cFailoverPrimaryChassisID.setStatus("current")


class _Hh3cFailoverPrimarySlotID_Type(Integer32):
    """Custom type hh3cFailoverPrimarySlotID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 255),
    )


_Hh3cFailoverPrimarySlotID_Type.__name__ = "Integer32"
_Hh3cFailoverPrimarySlotID_Object = MibTableColumn
hh3cFailoverPrimarySlotID = _Hh3cFailoverPrimarySlotID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 164, 2, 1, 1, 4),
    _Hh3cFailoverPrimarySlotID_Type()
)
hh3cFailoverPrimarySlotID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cFailoverPrimarySlotID.setStatus("current")


class _Hh3cFailoverPrimaryCpuID_Type(Integer32):
    """Custom type hh3cFailoverPrimaryCpuID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 7),
    )


_Hh3cFailoverPrimaryCpuID_Type.__name__ = "Integer32"
_Hh3cFailoverPrimaryCpuID_Object = MibTableColumn
hh3cFailoverPrimaryCpuID = _Hh3cFailoverPrimaryCpuID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 164, 2, 1, 1, 5),
    _Hh3cFailoverPrimaryCpuID_Type()
)
hh3cFailoverPrimaryCpuID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cFailoverPrimaryCpuID.setStatus("current")


class _Hh3cFailoverSecondaryChassisID_Type(Integer32):
    """Custom type hh3cFailoverSecondaryChassisID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 255),
    )


_Hh3cFailoverSecondaryChassisID_Type.__name__ = "Integer32"
_Hh3cFailoverSecondaryChassisID_Object = MibTableColumn
hh3cFailoverSecondaryChassisID = _Hh3cFailoverSecondaryChassisID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 164, 2, 1, 1, 6),
    _Hh3cFailoverSecondaryChassisID_Type()
)
hh3cFailoverSecondaryChassisID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cFailoverSecondaryChassisID.setStatus("current")


class _Hh3cFailoverSecondarySlotID_Type(Integer32):
    """Custom type hh3cFailoverSecondarySlotID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 255),
    )


_Hh3cFailoverSecondarySlotID_Type.__name__ = "Integer32"
_Hh3cFailoverSecondarySlotID_Object = MibTableColumn
hh3cFailoverSecondarySlotID = _Hh3cFailoverSecondarySlotID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 164, 2, 1, 1, 7),
    _Hh3cFailoverSecondarySlotID_Type()
)
hh3cFailoverSecondarySlotID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cFailoverSecondarySlotID.setStatus("current")


class _Hh3cFailoverSecondaryCpuID_Type(Integer32):
    """Custom type hh3cFailoverSecondaryCpuID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 7),
    )


_Hh3cFailoverSecondaryCpuID_Type.__name__ = "Integer32"
_Hh3cFailoverSecondaryCpuID_Object = MibTableColumn
hh3cFailoverSecondaryCpuID = _Hh3cFailoverSecondaryCpuID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 164, 2, 1, 1, 8),
    _Hh3cFailoverSecondaryCpuID_Type()
)
hh3cFailoverSecondaryCpuID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cFailoverSecondaryCpuID.setStatus("current")


class _Hh3cFailoverState_Type(Integer32):
    """Custom type hh3cFailoverState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("initial", 1),
          ("normal", 2),
          ("fault", 3))
    )


_Hh3cFailoverState_Type.__name__ = "Integer32"
_Hh3cFailoverState_Object = MibTableColumn
hh3cFailoverState = _Hh3cFailoverState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 164, 2, 1, 1, 9),
    _Hh3cFailoverState_Type()
)
hh3cFailoverState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFailoverState.setStatus("current")
_Hh3cFailoverRowStatus_Type = RowStatus
_Hh3cFailoverRowStatus_Object = MibTableColumn
hh3cFailoverRowStatus = _Hh3cFailoverRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 164, 2, 1, 1, 10),
    _Hh3cFailoverRowStatus_Type()
)
hh3cFailoverRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cFailoverRowStatus.setStatus("current")
_Hh3cFailoverNotification_ObjectIdentity = ObjectIdentity
hh3cFailoverNotification = _Hh3cFailoverNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 164, 3)
)
_Hh3cFailoverTrap_ObjectIdentity = ObjectIdentity
hh3cFailoverTrap = _Hh3cFailoverTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 164, 3, 0)
)

# Managed Objects groups


# Notification objects

hh3cFailoverCreate = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 164, 3, 0, 1)
)
hh3cFailoverCreate.setObjects(
      *(("HH3C-FAILOVER-MIB", "hh3cFailoverIndex"),
        ("HH3C-FAILOVER-MIB", "hh3cFailoverName"))
)
if mibBuilder.loadTexts:
    hh3cFailoverCreate.setStatus(
        "current"
    )

hh3cFailoverDelete = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 164, 3, 0, 2)
)
hh3cFailoverDelete.setObjects(
      *(("HH3C-FAILOVER-MIB", "hh3cFailoverIndex"),
        ("HH3C-FAILOVER-MIB", "hh3cFailoverName"))
)
if mibBuilder.loadTexts:
    hh3cFailoverDelete.setStatus(
        "current"
    )

hh3cFailoverPrimaryNodeAdd = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 164, 3, 0, 3)
)
hh3cFailoverPrimaryNodeAdd.setObjects(
      *(("HH3C-FAILOVER-MIB", "hh3cFailoverIndex"),
        ("HH3C-FAILOVER-MIB", "hh3cFailoverName"),
        ("HH3C-FAILOVER-MIB", "hh3cFailoverPrimaryChassisID"),
        ("HH3C-FAILOVER-MIB", "hh3cFailoverPrimarySlotID"),
        ("HH3C-FAILOVER-MIB", "hh3cFailoverPrimaryCpuID"))
)
if mibBuilder.loadTexts:
    hh3cFailoverPrimaryNodeAdd.setStatus(
        "current"
    )

hh3cFailoverPrimaryNodeRemove = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 164, 3, 0, 4)
)
hh3cFailoverPrimaryNodeRemove.setObjects(
      *(("HH3C-FAILOVER-MIB", "hh3cFailoverIndex"),
        ("HH3C-FAILOVER-MIB", "hh3cFailoverName"),
        ("HH3C-FAILOVER-MIB", "hh3cFailoverPrimaryChassisID"),
        ("HH3C-FAILOVER-MIB", "hh3cFailoverPrimarySlotID"),
        ("HH3C-FAILOVER-MIB", "hh3cFailoverPrimaryCpuID"))
)
if mibBuilder.loadTexts:
    hh3cFailoverPrimaryNodeRemove.setStatus(
        "current"
    )

hh3cFailoverSecondaryNodeAdd = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 164, 3, 0, 5)
)
hh3cFailoverSecondaryNodeAdd.setObjects(
      *(("HH3C-FAILOVER-MIB", "hh3cFailoverIndex"),
        ("HH3C-FAILOVER-MIB", "hh3cFailoverName"),
        ("HH3C-FAILOVER-MIB", "hh3cFailoverSecondaryChassisID"),
        ("HH3C-FAILOVER-MIB", "hh3cFailoverSecondarySlotID"),
        ("HH3C-FAILOVER-MIB", "hh3cFailoverSecondaryCpuID"))
)
if mibBuilder.loadTexts:
    hh3cFailoverSecondaryNodeAdd.setStatus(
        "current"
    )

hh3cFailoverSecondaryNodeRemove = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 164, 3, 0, 6)
)
hh3cFailoverSecondaryNodeRemove.setObjects(
      *(("HH3C-FAILOVER-MIB", "hh3cFailoverIndex"),
        ("HH3C-FAILOVER-MIB", "hh3cFailoverName"),
        ("HH3C-FAILOVER-MIB", "hh3cFailoverSecondaryChassisID"),
        ("HH3C-FAILOVER-MIB", "hh3cFailoverSecondarySlotID"),
        ("HH3C-FAILOVER-MIB", "hh3cFailoverSecondaryCpuID"))
)
if mibBuilder.loadTexts:
    hh3cFailoverSecondaryNodeRemove.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-FAILOVER-MIB",
    **{"hh3cFailover": hh3cFailover,
       "hh3cFailoverScalarObjects": hh3cFailoverScalarObjects,
       "hh3cFailoverMaxNum": hh3cFailoverMaxNum,
       "hh3cFailoverCurrentNum": hh3cFailoverCurrentNum,
       "hh3cFailoverTables": hh3cFailoverTables,
       "hh3cFailoverCfgTable": hh3cFailoverCfgTable,
       "hh3cFailoverCfgEntry": hh3cFailoverCfgEntry,
       "hh3cFailoverIndex": hh3cFailoverIndex,
       "hh3cFailoverName": hh3cFailoverName,
       "hh3cFailoverPrimaryChassisID": hh3cFailoverPrimaryChassisID,
       "hh3cFailoverPrimarySlotID": hh3cFailoverPrimarySlotID,
       "hh3cFailoverPrimaryCpuID": hh3cFailoverPrimaryCpuID,
       "hh3cFailoverSecondaryChassisID": hh3cFailoverSecondaryChassisID,
       "hh3cFailoverSecondarySlotID": hh3cFailoverSecondarySlotID,
       "hh3cFailoverSecondaryCpuID": hh3cFailoverSecondaryCpuID,
       "hh3cFailoverState": hh3cFailoverState,
       "hh3cFailoverRowStatus": hh3cFailoverRowStatus,
       "hh3cFailoverNotification": hh3cFailoverNotification,
       "hh3cFailoverTrap": hh3cFailoverTrap,
       "hh3cFailoverCreate": hh3cFailoverCreate,
       "hh3cFailoverDelete": hh3cFailoverDelete,
       "hh3cFailoverPrimaryNodeAdd": hh3cFailoverPrimaryNodeAdd,
       "hh3cFailoverPrimaryNodeRemove": hh3cFailoverPrimaryNodeRemove,
       "hh3cFailoverSecondaryNodeAdd": hh3cFailoverSecondaryNodeAdd,
       "hh3cFailoverSecondaryNodeRemove": hh3cFailoverSecondaryNodeRemove}
)
