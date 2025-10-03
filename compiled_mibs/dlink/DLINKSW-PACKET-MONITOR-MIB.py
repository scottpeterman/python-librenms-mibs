# SNMP MIB module (DLINKSW-PACKET-MONITOR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dlink\DLINKSW-PACKET-MONITOR-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:37:40 2025
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

(dlinkIndustrialCommon,) = mibBuilder.importSymbols(
    "DLINK-ID-REC-MIB",
    "dlinkIndustrialCommon")

(InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero",
    "ifIndex")

(VlanId,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId")

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


# MODULE-IDENTITY

dlinkSwPktMonitorMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 12)
)
if mibBuilder.loadTexts:
    dlinkSwPktMonitorMIB.setRevisions(
        ("2014-07-21 00:00",
         "2013-09-27 00:00",
         "2013-03-04 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DPktMonMIBNotifications_ObjectIdentity = ObjectIdentity
dPktMonMIBNotifications = _DPktMonMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 12, 0)
)
_DPktMonMIBObjects_ObjectIdentity = ObjectIdentity
dPktMonMIBObjects = _DPktMonMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 12, 1)
)
_DPktMonSessionTableCurrEntries_Type = Unsigned32
_DPktMonSessionTableCurrEntries_Object = MibScalar
dPktMonSessionTableCurrEntries = _DPktMonSessionTableCurrEntries_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 12, 1, 1),
    _DPktMonSessionTableCurrEntries_Type()
)
dPktMonSessionTableCurrEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dPktMonSessionTableCurrEntries.setStatus("current")
_DPktMonSessionTable_Object = MibTable
dPktMonSessionTable = _DPktMonSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 12, 1, 2)
)
if mibBuilder.loadTexts:
    dPktMonSessionTable.setStatus("current")
_DPktMonSessionEntry_Object = MibTableRow
dPktMonSessionEntry = _DPktMonSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 12, 1, 2, 1)
)
dPktMonSessionEntry.setIndexNames(
    (0, "DLINKSW-PACKET-MONITOR-MIB", "dPktMonSessionID"),
)
if mibBuilder.loadTexts:
    dPktMonSessionEntry.setStatus("current")


class _DPktMonSessionID_Type(Integer32):
    """Custom type dPktMonSessionID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 80),
    )


_DPktMonSessionID_Type.__name__ = "Integer32"
_DPktMonSessionID_Object = MibTableColumn
dPktMonSessionID = _DPktMonSessionID_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 12, 1, 2, 1, 1),
    _DPktMonSessionID_Type()
)
dPktMonSessionID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dPktMonSessionID.setStatus("current")


class _DPktMonSessionSessionType_Type(Integer32):
    """Custom type dPktMonSessionSessionType based on Integer32"""
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
        *(("none", 0),
          ("localSession", 1),
          ("remoteSourceSession", 2),
          ("remoteDestinationSession", 3))
    )


_DPktMonSessionSessionType_Type.__name__ = "Integer32"
_DPktMonSessionSessionType_Object = MibTableColumn
dPktMonSessionSessionType = _DPktMonSessionSessionType_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 12, 1, 2, 1, 2),
    _DPktMonSessionSessionType_Type()
)
dPktMonSessionSessionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dPktMonSessionSessionType.setStatus("current")


class _DPktMonSessionDestRemoteVlanId_Type(Integer32):
    """Custom type dPktMonSessionDestRemoteVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2, 4094),
    )


_DPktMonSessionDestRemoteVlanId_Type.__name__ = "Integer32"
_DPktMonSessionDestRemoteVlanId_Object = MibTableColumn
dPktMonSessionDestRemoteVlanId = _DPktMonSessionDestRemoteVlanId_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 12, 1, 2, 1, 3),
    _DPktMonSessionDestRemoteVlanId_Type()
)
dPktMonSessionDestRemoteVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dPktMonSessionDestRemoteVlanId.setStatus("current")


class _DPktMonSessionSourceRemoteVlanId_Type(Integer32):
    """Custom type dPktMonSessionSourceRemoteVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2, 4094),
    )


_DPktMonSessionSourceRemoteVlanId_Type.__name__ = "Integer32"
_DPktMonSessionSourceRemoteVlanId_Object = MibTableColumn
dPktMonSessionSourceRemoteVlanId = _DPktMonSessionSourceRemoteVlanId_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 12, 1, 2, 1, 4),
    _DPktMonSessionSourceRemoteVlanId_Type()
)
dPktMonSessionSourceRemoteVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dPktMonSessionSourceRemoteVlanId.setStatus("current")
_DPktMonSessionDestInterface_Type = InterfaceIndexOrZero
_DPktMonSessionDestInterface_Object = MibTableColumn
dPktMonSessionDestInterface = _DPktMonSessionDestInterface_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 12, 1, 2, 1, 5),
    _DPktMonSessionDestInterface_Type()
)
dPktMonSessionDestInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dPktMonSessionDestInterface.setStatus("current")
_DPktMonSessionRowStatus_Type = RowStatus
_DPktMonSessionRowStatus_Object = MibTableColumn
dPktMonSessionRowStatus = _DPktMonSessionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 12, 1, 2, 1, 6),
    _DPktMonSessionRowStatus_Type()
)
dPktMonSessionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dPktMonSessionRowStatus.setStatus("current")
_DPktMonSessionSrcIfObjects_ObjectIdentity = ObjectIdentity
dPktMonSessionSrcIfObjects = _DPktMonSessionSrcIfObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 12, 1, 3)
)
if mibBuilder.loadTexts:
    dPktMonSessionSrcIfObjects.setStatus("current")
_DPktMonSessionSrcRxIfTable_Object = MibTable
dPktMonSessionSrcRxIfTable = _DPktMonSessionSrcRxIfTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 12, 1, 3, 1)
)
if mibBuilder.loadTexts:
    dPktMonSessionSrcRxIfTable.setStatus("current")
_DPktMonSessionSrcRxIfEntry_Object = MibTableRow
dPktMonSessionSrcRxIfEntry = _DPktMonSessionSrcRxIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 12, 1, 3, 1, 1)
)
dPktMonSessionSrcRxIfEntry.setIndexNames(
    (0, "DLINKSW-PACKET-MONITOR-MIB", "dPktMonSessionID"),
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dPktMonSessionSrcRxIfEntry.setStatus("current")
_DPktMonSessionSrcRxIfRowStatus_Type = RowStatus
_DPktMonSessionSrcRxIfRowStatus_Object = MibTableColumn
dPktMonSessionSrcRxIfRowStatus = _DPktMonSessionSrcRxIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 12, 1, 3, 1, 1, 1),
    _DPktMonSessionSrcRxIfRowStatus_Type()
)
dPktMonSessionSrcRxIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dPktMonSessionSrcRxIfRowStatus.setStatus("current")
_DPktMonSessionSrcTxIfTable_Object = MibTable
dPktMonSessionSrcTxIfTable = _DPktMonSessionSrcTxIfTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 12, 1, 3, 2)
)
if mibBuilder.loadTexts:
    dPktMonSessionSrcTxIfTable.setStatus("current")
_DPktMonSessionSrcTxIfEntry_Object = MibTableRow
dPktMonSessionSrcTxIfEntry = _DPktMonSessionSrcTxIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 12, 1, 3, 2, 1)
)
dPktMonSessionSrcTxIfEntry.setIndexNames(
    (0, "DLINKSW-PACKET-MONITOR-MIB", "dPktMonSessionID"),
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dPktMonSessionSrcTxIfEntry.setStatus("current")
_DPktMonSessionSrcTxIfRowStatus_Type = RowStatus
_DPktMonSessionSrcTxIfRowStatus_Object = MibTableColumn
dPktMonSessionSrcTxIfRowStatus = _DPktMonSessionSrcTxIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 12, 1, 3, 2, 1, 1),
    _DPktMonSessionSrcTxIfRowStatus_Type()
)
dPktMonSessionSrcTxIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dPktMonSessionSrcTxIfRowStatus.setStatus("current")


class _DPktMonSessionSrcTxIfStgState_Type(Integer32):
    """Custom type dPktMonSessionSrcTxIfStgState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no-care", 1),
          ("forwarding", 2))
    )


_DPktMonSessionSrcTxIfStgState_Type.__name__ = "Integer32"
_DPktMonSessionSrcTxIfStgState_Object = MibTableColumn
dPktMonSessionSrcTxIfStgState = _DPktMonSessionSrcTxIfStgState_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 12, 1, 3, 2, 1, 2),
    _DPktMonSessionSrcTxIfStgState_Type()
)
dPktMonSessionSrcTxIfStgState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dPktMonSessionSrcTxIfStgState.setStatus("current")
_DPktMonSessionSrcDropIfTable_Object = MibTable
dPktMonSessionSrcDropIfTable = _DPktMonSessionSrcDropIfTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 12, 1, 3, 3)
)
if mibBuilder.loadTexts:
    dPktMonSessionSrcDropIfTable.setStatus("current")
_DPktMonSessionSrcDropIfEntry_Object = MibTableRow
dPktMonSessionSrcDropIfEntry = _DPktMonSessionSrcDropIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 12, 1, 3, 3, 1)
)
dPktMonSessionSrcDropIfEntry.setIndexNames(
    (0, "DLINKSW-PACKET-MONITOR-MIB", "dPktMonSessionID"),
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dPktMonSessionSrcDropIfEntry.setStatus("current")
_DPktMonSessionSrcDropIfRowStatus_Type = RowStatus
_DPktMonSessionSrcDropIfRowStatus_Object = MibTableColumn
dPktMonSessionSrcDropIfRowStatus = _DPktMonSessionSrcDropIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 12, 1, 3, 3, 1, 1),
    _DPktMonSessionSrcDropIfRowStatus_Type()
)
dPktMonSessionSrcDropIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dPktMonSessionSrcDropIfRowStatus.setStatus("current")
_DPktMonSessionSrcAclTable_Object = MibTable
dPktMonSessionSrcAclTable = _DPktMonSessionSrcAclTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 12, 1, 4)
)
if mibBuilder.loadTexts:
    dPktMonSessionSrcAclTable.setStatus("current")
_DPktMonSessionSrcAclEntry_Object = MibTableRow
dPktMonSessionSrcAclEntry = _DPktMonSessionSrcAclEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 12, 1, 4, 1)
)
dPktMonSessionSrcAclEntry.setIndexNames(
    (0, "DLINKSW-PACKET-MONITOR-MIB", "dPktMonSessionID"),
    (0, "DLINKSW-PACKET-MONITOR-MIB", "dPktMonSessionSrcAclName"),
)
if mibBuilder.loadTexts:
    dPktMonSessionSrcAclEntry.setStatus("current")


class _DPktMonSessionSrcAclName_Type(DisplayString):
    """Custom type dPktMonSessionSrcAclName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_DPktMonSessionSrcAclName_Type.__name__ = "DisplayString"
_DPktMonSessionSrcAclName_Object = MibTableColumn
dPktMonSessionSrcAclName = _DPktMonSessionSrcAclName_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 12, 1, 4, 1, 1),
    _DPktMonSessionSrcAclName_Type()
)
dPktMonSessionSrcAclName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dPktMonSessionSrcAclName.setStatus("current")
_DPktMonSessionSrcAclRowStatus_Type = RowStatus
_DPktMonSessionSrcAclRowStatus_Object = MibTableColumn
dPktMonSessionSrcAclRowStatus = _DPktMonSessionSrcAclRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 12, 1, 4, 1, 2),
    _DPktMonSessionSrcAclRowStatus_Type()
)
dPktMonSessionSrcAclRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dPktMonSessionSrcAclRowStatus.setStatus("current")
_DPktMonRspanVlanTable_Object = MibTable
dPktMonRspanVlanTable = _DPktMonRspanVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 12, 1, 5)
)
if mibBuilder.loadTexts:
    dPktMonRspanVlanTable.setStatus("current")
_DPktMonRspanVlanEntry_Object = MibTableRow
dPktMonRspanVlanEntry = _DPktMonRspanVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 12, 1, 5, 1)
)
dPktMonRspanVlanEntry.setIndexNames(
    (0, "DLINKSW-PACKET-MONITOR-MIB", "dPktMonRspanVlanId"),
)
if mibBuilder.loadTexts:
    dPktMonRspanVlanEntry.setStatus("current")
_DPktMonRspanVlanId_Type = VlanId
_DPktMonRspanVlanId_Object = MibTableColumn
dPktMonRspanVlanId = _DPktMonRspanVlanId_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 12, 1, 5, 1, 1),
    _DPktMonRspanVlanId_Type()
)
dPktMonRspanVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dPktMonRspanVlanId.setStatus("current")
_DPktMonRspanVlanRowStatus_Type = RowStatus
_DPktMonRspanVlanRowStatus_Object = MibTableColumn
dPktMonRspanVlanRowStatus = _DPktMonRspanVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 12, 1, 5, 1, 2),
    _DPktMonRspanVlanRowStatus_Type()
)
dPktMonRspanVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dPktMonRspanVlanRowStatus.setStatus("current")
_DPktMonSessionDestRemoteReplaceVlanTable_Object = MibTable
dPktMonSessionDestRemoteReplaceVlanTable = _DPktMonSessionDestRemoteReplaceVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 12, 1, 6)
)
if mibBuilder.loadTexts:
    dPktMonSessionDestRemoteReplaceVlanTable.setStatus("current")
_DPktMonSessionDestRemoteReplaceVlanEntry_Object = MibTableRow
dPktMonSessionDestRemoteReplaceVlanEntry = _DPktMonSessionDestRemoteReplaceVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 12, 1, 6, 1)
)
dPktMonSessionDestRemoteReplaceVlanEntry.setIndexNames(
    (0, "DLINKSW-PACKET-MONITOR-MIB", "dPktMonSessionID"),
    (0, "DLINKSW-PACKET-MONITOR-MIB", "dPktMonSessionDestRemoteAccessListName"),
    (0, "DLINKSW-PACKET-MONITOR-MIB", "dPktMonSessionDestRemoteReplaceVlanId"),
)
if mibBuilder.loadTexts:
    dPktMonSessionDestRemoteReplaceVlanEntry.setStatus("current")


class _DPktMonSessionDestRemoteAccessListName_Type(DisplayString):
    """Custom type dPktMonSessionDestRemoteAccessListName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_DPktMonSessionDestRemoteAccessListName_Type.__name__ = "DisplayString"
_DPktMonSessionDestRemoteAccessListName_Object = MibTableColumn
dPktMonSessionDestRemoteAccessListName = _DPktMonSessionDestRemoteAccessListName_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 12, 1, 6, 1, 1),
    _DPktMonSessionDestRemoteAccessListName_Type()
)
dPktMonSessionDestRemoteAccessListName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dPktMonSessionDestRemoteAccessListName.setStatus("current")
_DPktMonSessionDestRemoteReplaceVlanId_Type = VlanId
_DPktMonSessionDestRemoteReplaceVlanId_Object = MibTableColumn
dPktMonSessionDestRemoteReplaceVlanId = _DPktMonSessionDestRemoteReplaceVlanId_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 12, 1, 6, 1, 2),
    _DPktMonSessionDestRemoteReplaceVlanId_Type()
)
dPktMonSessionDestRemoteReplaceVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dPktMonSessionDestRemoteReplaceVlanId.setStatus("current")
_DPktMonSessionDestRemoteReplaceVlanRowStatus_Type = RowStatus
_DPktMonSessionDestRemoteReplaceVlanRowStatus_Object = MibTableColumn
dPktMonSessionDestRemoteReplaceVlanRowStatus = _DPktMonSessionDestRemoteReplaceVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 12, 1, 6, 1, 3),
    _DPktMonSessionDestRemoteReplaceVlanRowStatus_Type()
)
dPktMonSessionDestRemoteReplaceVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dPktMonSessionDestRemoteReplaceVlanRowStatus.setStatus("current")
_DPktMonMIBConformance_ObjectIdentity = ObjectIdentity
dPktMonMIBConformance = _DPktMonMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 12, 2)
)
_DPktMonMIBCompliances_ObjectIdentity = ObjectIdentity
dPktMonMIBCompliances = _DPktMonMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 12, 2, 1)
)
_DPktMonMIBGroups_ObjectIdentity = ObjectIdentity
dPktMonMIBGroups = _DPktMonMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 12, 2, 2)
)

# Managed Objects groups

dPktMonBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 12, 2, 2, 1)
)
dPktMonBasicGroup.setObjects(
      *(("DLINKSW-PACKET-MONITOR-MIB", "dPktMonSessionTableCurrEntries"),
        ("DLINKSW-PACKET-MONITOR-MIB", "dPktMonSessionDestInterface"),
        ("DLINKSW-PACKET-MONITOR-MIB", "dPktMonSessionRowStatus"),
        ("DLINKSW-PACKET-MONITOR-MIB", "dPktMonSessionSrcRxIfRowStatus"),
        ("DLINKSW-PACKET-MONITOR-MIB", "dPktMonSessionSrcTxIfRowStatus"))
)
if mibBuilder.loadTexts:
    dPktMonBasicGroup.setStatus("current")

dPktMonRspanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 12, 2, 2, 2)
)
dPktMonRspanGroup.setObjects(
      *(("DLINKSW-PACKET-MONITOR-MIB", "dPktMonSessionSessionType"),
        ("DLINKSW-PACKET-MONITOR-MIB", "dPktMonSessionDestRemoteVlanId"),
        ("DLINKSW-PACKET-MONITOR-MIB", "dPktMonSessionSourceRemoteVlanId"),
        ("DLINKSW-PACKET-MONITOR-MIB", "dPktMonRspanVlanRowStatus"))
)
if mibBuilder.loadTexts:
    dPktMonRspanGroup.setStatus("current")

dPktMonFlowBasedMirrorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 12, 2, 2, 3)
)
dPktMonFlowBasedMirrorGroup.setObjects(
    ("DLINKSW-PACKET-MONITOR-MIB", "dPktMonSessionSrcAclRowStatus")
)
if mibBuilder.loadTexts:
    dPktMonFlowBasedMirrorGroup.setStatus("current")

dPktMonMonitorDropPktGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 12, 2, 2, 4)
)
dPktMonMonitorDropPktGroup.setObjects(
    ("DLINKSW-PACKET-MONITOR-MIB", "dPktMonSessionSrcDropIfRowStatus")
)
if mibBuilder.loadTexts:
    dPktMonMonitorDropPktGroup.setStatus("current")

dPktMonDestRemoteReplaceVlanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 12, 2, 2, 5)
)
dPktMonDestRemoteReplaceVlanGroup.setObjects(
    ("DLINKSW-PACKET-MONITOR-MIB", "dPktMonSessionDestRemoteReplaceVlanRowStatus")
)
if mibBuilder.loadTexts:
    dPktMonDestRemoteReplaceVlanGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

dPktMonMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 171, 14, 12, 2, 1, 1)
)
dPktMonMIBCompliance.setObjects(
      *(("DLINKSW-PACKET-MONITOR-MIB", "dPktMonBasicGroup"),
        ("DLINKSW-PACKET-MONITOR-MIB", "dPktMonRspanGroup"),
        ("DLINKSW-PACKET-MONITOR-MIB", "dPktMonFlowBasedMirrorGroup"),
        ("DLINKSW-PACKET-MONITOR-MIB", "dPktMonMonitorDropPktGroup"),
        ("DLINKSW-PACKET-MONITOR-MIB", "dPktMonDestRemoteReplaceVlanGroup"))
)
if mibBuilder.loadTexts:
    dPktMonMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLINKSW-PACKET-MONITOR-MIB",
    **{"dlinkSwPktMonitorMIB": dlinkSwPktMonitorMIB,
       "dPktMonMIBNotifications": dPktMonMIBNotifications,
       "dPktMonMIBObjects": dPktMonMIBObjects,
       "dPktMonSessionTableCurrEntries": dPktMonSessionTableCurrEntries,
       "dPktMonSessionTable": dPktMonSessionTable,
       "dPktMonSessionEntry": dPktMonSessionEntry,
       "dPktMonSessionID": dPktMonSessionID,
       "dPktMonSessionSessionType": dPktMonSessionSessionType,
       "dPktMonSessionDestRemoteVlanId": dPktMonSessionDestRemoteVlanId,
       "dPktMonSessionSourceRemoteVlanId": dPktMonSessionSourceRemoteVlanId,
       "dPktMonSessionDestInterface": dPktMonSessionDestInterface,
       "dPktMonSessionRowStatus": dPktMonSessionRowStatus,
       "dPktMonSessionSrcIfObjects": dPktMonSessionSrcIfObjects,
       "dPktMonSessionSrcRxIfTable": dPktMonSessionSrcRxIfTable,
       "dPktMonSessionSrcRxIfEntry": dPktMonSessionSrcRxIfEntry,
       "dPktMonSessionSrcRxIfRowStatus": dPktMonSessionSrcRxIfRowStatus,
       "dPktMonSessionSrcTxIfTable": dPktMonSessionSrcTxIfTable,
       "dPktMonSessionSrcTxIfEntry": dPktMonSessionSrcTxIfEntry,
       "dPktMonSessionSrcTxIfRowStatus": dPktMonSessionSrcTxIfRowStatus,
       "dPktMonSessionSrcTxIfStgState": dPktMonSessionSrcTxIfStgState,
       "dPktMonSessionSrcDropIfTable": dPktMonSessionSrcDropIfTable,
       "dPktMonSessionSrcDropIfEntry": dPktMonSessionSrcDropIfEntry,
       "dPktMonSessionSrcDropIfRowStatus": dPktMonSessionSrcDropIfRowStatus,
       "dPktMonSessionSrcAclTable": dPktMonSessionSrcAclTable,
       "dPktMonSessionSrcAclEntry": dPktMonSessionSrcAclEntry,
       "dPktMonSessionSrcAclName": dPktMonSessionSrcAclName,
       "dPktMonSessionSrcAclRowStatus": dPktMonSessionSrcAclRowStatus,
       "dPktMonRspanVlanTable": dPktMonRspanVlanTable,
       "dPktMonRspanVlanEntry": dPktMonRspanVlanEntry,
       "dPktMonRspanVlanId": dPktMonRspanVlanId,
       "dPktMonRspanVlanRowStatus": dPktMonRspanVlanRowStatus,
       "dPktMonSessionDestRemoteReplaceVlanTable": dPktMonSessionDestRemoteReplaceVlanTable,
       "dPktMonSessionDestRemoteReplaceVlanEntry": dPktMonSessionDestRemoteReplaceVlanEntry,
       "dPktMonSessionDestRemoteAccessListName": dPktMonSessionDestRemoteAccessListName,
       "dPktMonSessionDestRemoteReplaceVlanId": dPktMonSessionDestRemoteReplaceVlanId,
       "dPktMonSessionDestRemoteReplaceVlanRowStatus": dPktMonSessionDestRemoteReplaceVlanRowStatus,
       "dPktMonMIBConformance": dPktMonMIBConformance,
       "dPktMonMIBCompliances": dPktMonMIBCompliances,
       "dPktMonMIBCompliance": dPktMonMIBCompliance,
       "dPktMonMIBGroups": dPktMonMIBGroups,
       "dPktMonBasicGroup": dPktMonBasicGroup,
       "dPktMonRspanGroup": dPktMonRspanGroup,
       "dPktMonFlowBasedMirrorGroup": dPktMonFlowBasedMirrorGroup,
       "dPktMonMonitorDropPktGroup": dPktMonMonitorDropPktGroup,
       "dPktMonDestRemoteReplaceVlanGroup": dPktMonDestRemoteReplaceVlanGroup}
)
