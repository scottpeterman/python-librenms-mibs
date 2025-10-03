# SNMP MIB module (UBQS-LAG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ubiquoss\UBQS-LAG-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:33:20 2025
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

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

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

(ubiMgmtv2,) = mibBuilder.importSymbols(
    "UBQS-SMI",
    "ubiMgmtv2")

(UbiPortList,) = mibBuilder.importSymbols(
    "UBQS-TC",
    "UbiPortList")


# MODULE-IDENTITY

ubiLagMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 100, 16)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class UbiLagList(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("src-mac", 1),
          ("dst-mac", 2),
          ("src-dst-mac", 3),
          ("src-ip", 4),
          ("dst-ip", 5),
          ("src-dst-ip", 6),
          ("src-port", 7),
          ("dst-port", 8),
          ("src-dst-port", 9))
    )


# MIB Managed Objects in the order of their OIDs

_UbiLagMIBNotificationsPrefix_ObjectIdentity = ObjectIdentity
ubiLagMIBNotificationsPrefix = _UbiLagMIBNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 100, 16, 0)
)
_UbiBackupIntfMIBNotifications_ObjectIdentity = ObjectIdentity
ubiBackupIntfMIBNotifications = _UbiBackupIntfMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 100, 16, 0, 1)
)
_UbiLagMIBObjects_ObjectIdentity = ObjectIdentity
ubiLagMIBObjects = _UbiLagMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 100, 16, 1)
)
_UbiAgg_ObjectIdentity = ObjectIdentity
ubiAgg = _UbiAgg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 100, 16, 1, 1)
)
_UbiAggTable_Object = MibTable
ubiAggTable = _UbiAggTable_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 16, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ubiAggTable.setStatus("current")
_UbiAggEntry_Object = MibTableRow
ubiAggEntry = _UbiAggEntry_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 16, 1, 1, 1, 1)
)
ubiAggEntry.setIndexNames(
    (0, "UBQS-LAG-MIB", "ubiLagAggId"),
)
if mibBuilder.loadTexts:
    ubiAggEntry.setStatus("current")
_UbiAggId_Type = Integer32
_UbiAggId_Object = MibTableColumn
ubiAggId = _UbiAggId_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 16, 1, 1, 1, 1, 1),
    _UbiAggId_Type()
)
ubiAggId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiAggId.setStatus("current")


class _UbiAggDelete_Type(Integer32):
    """Custom type ubiAggDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("set", 1))
    )


_UbiAggDelete_Type.__name__ = "Integer32"
_UbiAggDelete_Object = MibTableColumn
ubiAggDelete = _UbiAggDelete_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 16, 1, 1, 1, 1, 2),
    _UbiAggDelete_Type()
)
ubiAggDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiAggDelete.setStatus("current")
_UbiAggPortTable_Object = MibTable
ubiAggPortTable = _UbiAggPortTable_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 16, 1, 1, 2)
)
if mibBuilder.loadTexts:
    ubiAggPortTable.setStatus("current")
_UbiAggPortEntry_Object = MibTableRow
ubiAggPortEntry = _UbiAggPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 16, 1, 1, 2, 1)
)
ubiAggPortEntry.setIndexNames(
    (0, "UBQS-LAG-MIB", "ubiLagAggId"),
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ubiAggPortEntry.setStatus("current")


class _UbiAggPortAggMode_Type(Integer32):
    """Custom type ubiAggPortAggMode based on Integer32"""
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
        *(("other", 1),
          ("on", 2),
          ("off", 3),
          ("active", 4),
          ("passive", 5))
    )


_UbiAggPortAggMode_Type.__name__ = "Integer32"
_UbiAggPortAggMode_Object = MibTableColumn
ubiAggPortAggMode = _UbiAggPortAggMode_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 16, 1, 1, 2, 1, 1),
    _UbiAggPortAggMode_Type()
)
ubiAggPortAggMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ubiAggPortAggMode.setStatus("current")
_UbiAggPortRowStatus_Type = RowStatus
_UbiAggPortRowStatus_Object = MibTableColumn
ubiAggPortRowStatus = _UbiAggPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 16, 1, 1, 2, 1, 2),
    _UbiAggPortRowStatus_Type()
)
ubiAggPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ubiAggPortRowStatus.setStatus("current")
_UbiLagLoadBalanceTable_Object = MibTable
ubiLagLoadBalanceTable = _UbiLagLoadBalanceTable_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 16, 1, 1, 3)
)
if mibBuilder.loadTexts:
    ubiLagLoadBalanceTable.setStatus("current")
_UbiLagLoadBalanceEntry_Object = MibTableRow
ubiLagLoadBalanceEntry = _UbiLagLoadBalanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 16, 1, 1, 3, 1)
)
ubiLagLoadBalanceEntry.setIndexNames(
    (0, "UBQS-LAG-MIB", "ubiLagLoadBalanceAggId"),
)
if mibBuilder.loadTexts:
    ubiLagLoadBalanceEntry.setStatus("current")


class _UbiLagLoadBalanceAggId_Type(Integer32):
    """Custom type ubiLagLoadBalanceAggId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_UbiLagLoadBalanceAggId_Type.__name__ = "Integer32"
_UbiLagLoadBalanceAggId_Object = MibTableColumn
ubiLagLoadBalanceAggId = _UbiLagLoadBalanceAggId_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 16, 1, 1, 3, 1, 1),
    _UbiLagLoadBalanceAggId_Type()
)
ubiLagLoadBalanceAggId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ubiLagLoadBalanceAggId.setStatus("current")
_UbiLagLoadBalanceMode_Type = UbiLagList
_UbiLagLoadBalanceMode_Object = MibTableColumn
ubiLagLoadBalanceMode = _UbiLagLoadBalanceMode_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 16, 1, 1, 3, 1, 2),
    _UbiLagLoadBalanceMode_Type()
)
ubiLagLoadBalanceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiLagLoadBalanceMode.setStatus("current")
_UbiRedundancyPort_ObjectIdentity = ObjectIdentity
ubiRedundancyPort = _UbiRedundancyPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 100, 16, 1, 2)
)
_UbiRedundancyPortTable_Object = MibTable
ubiRedundancyPortTable = _UbiRedundancyPortTable_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 16, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ubiRedundancyPortTable.setStatus("current")
_UbiRedundancyPortEntry_Object = MibTableRow
ubiRedundancyPortEntry = _UbiRedundancyPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 16, 1, 2, 1, 1)
)
ubiRedundancyPortEntry.setIndexNames(
    (0, "UBQS-LAG-MIB", "ubiReduIfIndex"),
)
if mibBuilder.loadTexts:
    ubiRedundancyPortEntry.setStatus("current")
_UbiReduIfIndex_Type = InterfaceIndex
_UbiReduIfIndex_Object = MibTableColumn
ubiReduIfIndex = _UbiReduIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 16, 1, 2, 1, 1, 1),
    _UbiReduIfIndex_Type()
)
ubiReduIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiReduIfIndex.setStatus("current")
_UbiReduBackupIfIndex_Type = InterfaceIndex
_UbiReduBackupIfIndex_Object = MibTableColumn
ubiReduBackupIfIndex = _UbiReduBackupIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 16, 1, 2, 1, 1, 2),
    _UbiReduBackupIfIndex_Type()
)
ubiReduBackupIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiReduBackupIfIndex.setStatus("current")
_UbiReduIfName_Type = DisplayString
_UbiReduIfName_Object = MibTableColumn
ubiReduIfName = _UbiReduIfName_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 16, 1, 2, 1, 1, 3),
    _UbiReduIfName_Type()
)
ubiReduIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiReduIfName.setStatus("current")
_UbiReduLink_Type = Integer32
_UbiReduLink_Object = MibTableColumn
ubiReduLink = _UbiReduLink_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 16, 1, 2, 1, 1, 4),
    _UbiReduLink_Type()
)
ubiReduLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiReduLink.setStatus("current")
_UbiReduMode_Type = Integer32
_UbiReduMode_Object = MibTableColumn
ubiReduMode = _UbiReduMode_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 16, 1, 2, 1, 1, 5),
    _UbiReduMode_Type()
)
ubiReduMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiReduMode.setStatus("current")
_UbiReduRvt_Type = Integer32
_UbiReduRvt_Object = MibTableColumn
ubiReduRvt = _UbiReduRvt_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 16, 1, 2, 1, 1, 6),
    _UbiReduRvt_Type()
)
ubiReduRvt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiReduRvt.setStatus("current")
_UbiReduBackupIf_Type = DisplayString
_UbiReduBackupIf_Object = MibTableColumn
ubiReduBackupIf = _UbiReduBackupIf_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 16, 1, 2, 1, 1, 7),
    _UbiReduBackupIf_Type()
)
ubiReduBackupIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiReduBackupIf.setStatus("current")
_UbiReduStatus_Type = Integer32
_UbiReduStatus_Object = MibTableColumn
ubiReduStatus = _UbiReduStatus_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 16, 1, 2, 1, 1, 8),
    _UbiReduStatus_Type()
)
ubiReduStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiReduStatus.setStatus("current")
_UbiReduWtr_Type = Integer32
_UbiReduWtr_Object = MibTableColumn
ubiReduWtr = _UbiReduWtr_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 16, 1, 2, 1, 1, 9),
    _UbiReduWtr_Type()
)
ubiReduWtr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiReduWtr.setStatus("current")
_UbiReduHoldoff_Type = Integer32
_UbiReduHoldoff_Object = MibTableColumn
ubiReduHoldoff = _UbiReduHoldoff_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 16, 1, 2, 1, 1, 10),
    _UbiReduHoldoff_Type()
)
ubiReduHoldoff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiReduHoldoff.setStatus("current")
_UbiReduRowStatus_Type = RowStatus
_UbiReduRowStatus_Object = MibTableColumn
ubiReduRowStatus = _UbiReduRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 16, 1, 2, 1, 1, 11),
    _UbiReduRowStatus_Type()
)
ubiReduRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ubiReduRowStatus.setStatus("current")
_UbiLagMIBConformance_ObjectIdentity = ObjectIdentity
ubiLagMIBConformance = _UbiLagMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 100, 16, 2)
)
_UbiLagMIBCompliances_ObjectIdentity = ObjectIdentity
ubiLagMIBCompliances = _UbiLagMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 100, 16, 2, 1)
)
_UbiLagMIBGroups_ObjectIdentity = ObjectIdentity
ubiLagMIBGroups = _UbiLagMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 100, 16, 2, 2)
)

# Managed Objects groups

ubiAggGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7800, 100, 16, 2, 2, 1)
)
ubiAggGroup.setObjects(
      *(("UBQS-LAG-MIB", "ubiAggDelete"),
        ("UBQS-LAG-MIB", "ubiAggId"),
        ("UBQS-LAG-MIB", "ubiAggAdminStatus"),
        ("UBQS-LAG-MIB", "ubiAggRowStatus"))
)
if mibBuilder.loadTexts:
    ubiAggGroup.setStatus("current")


# Notification objects

ubiBackupIntfSwitchover = NotificationType(
    (1, 3, 6, 1, 4, 1, 7800, 100, 16, 0, 1, 1)
)
ubiBackupIntfSwitchover.setObjects(
      *(("UBQS-LAG-MIB", "ubiReduIfIndex"),
        ("UBQS-LAG-MIB", "ubiReduBackupIfIndex"),
        ("UBQS-LAG-MIB", "ubiReduIfName"),
        ("UBQS-LAG-MIB", "ubiReduLink"),
        ("UBQS-LAG-MIB", "ubiReduMode"),
        ("UBQS-LAG-MIB", "ubiReduRvt"),
        ("UBQS-LAG-MIB", "ubiReduBackupIf"))
)
if mibBuilder.loadTexts:
    ubiBackupIntfSwitchover.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

ubiLagMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7800, 100, 16, 2, 1, 1)
)
ubiLagMIBCompliance.setObjects(
    ("UBQS-LAG-MIB", "ubiAggGroup")
)
if mibBuilder.loadTexts:
    ubiLagMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "UBQS-LAG-MIB",
    **{"UbiLagList": UbiLagList,
       "ubiLagMIB": ubiLagMIB,
       "ubiLagMIBNotificationsPrefix": ubiLagMIBNotificationsPrefix,
       "ubiBackupIntfMIBNotifications": ubiBackupIntfMIBNotifications,
       "ubiBackupIntfSwitchover": ubiBackupIntfSwitchover,
       "ubiLagMIBObjects": ubiLagMIBObjects,
       "ubiAgg": ubiAgg,
       "ubiAggTable": ubiAggTable,
       "ubiAggEntry": ubiAggEntry,
       "ubiAggId": ubiAggId,
       "ubiAggDelete": ubiAggDelete,
       "ubiAggPortTable": ubiAggPortTable,
       "ubiAggPortEntry": ubiAggPortEntry,
       "ubiAggPortAggMode": ubiAggPortAggMode,
       "ubiAggPortRowStatus": ubiAggPortRowStatus,
       "ubiLagLoadBalanceTable": ubiLagLoadBalanceTable,
       "ubiLagLoadBalanceEntry": ubiLagLoadBalanceEntry,
       "ubiLagLoadBalanceAggId": ubiLagLoadBalanceAggId,
       "ubiLagLoadBalanceMode": ubiLagLoadBalanceMode,
       "ubiRedundancyPort": ubiRedundancyPort,
       "ubiRedundancyPortTable": ubiRedundancyPortTable,
       "ubiRedundancyPortEntry": ubiRedundancyPortEntry,
       "ubiReduIfIndex": ubiReduIfIndex,
       "ubiReduBackupIfIndex": ubiReduBackupIfIndex,
       "ubiReduIfName": ubiReduIfName,
       "ubiReduLink": ubiReduLink,
       "ubiReduMode": ubiReduMode,
       "ubiReduRvt": ubiReduRvt,
       "ubiReduBackupIf": ubiReduBackupIf,
       "ubiReduStatus": ubiReduStatus,
       "ubiReduWtr": ubiReduWtr,
       "ubiReduHoldoff": ubiReduHoldoff,
       "ubiReduRowStatus": ubiReduRowStatus,
       "ubiLagMIBConformance": ubiLagMIBConformance,
       "ubiLagMIBCompliances": ubiLagMIBCompliances,
       "ubiLagMIBCompliance": ubiLagMIBCompliance,
       "ubiLagMIBGroups": ubiLagMIBGroups,
       "ubiAggGroup": ubiAggGroup}
)
