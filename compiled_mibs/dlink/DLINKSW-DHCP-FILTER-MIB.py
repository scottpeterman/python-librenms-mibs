# SNMP MIB module (DLINKSW-DHCP-FILTER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dlink\DLINKSW-DHCP-FILTER-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:36:49 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
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

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

dlinkSwDhcpFilterMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 133)
)
if mibBuilder.loadTexts:
    dlinkSwDhcpFilterMIB.setRevisions(
        ("2013-07-19 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DDhcpFilterMIBNotifications_ObjectIdentity = ObjectIdentity
dDhcpFilterMIBNotifications = _DDhcpFilterMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 133, 0)
)
_DDhcpFilterMIBObjects_ObjectIdentity = ObjectIdentity
dDhcpFilterMIBObjects = _DDhcpFilterMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 133, 1)
)
_DDhcpFilterGlobalObjects_ObjectIdentity = ObjectIdentity
dDhcpFilterGlobalObjects = _DDhcpFilterGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 133, 1, 1)
)


class _DDhcpFilterLogBufferSize_Type(Unsigned32):
    """Custom type dDhcpFilterLogBufferSize based on Unsigned32"""
    defaultValue = 32

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_DDhcpFilterLogBufferSize_Type.__name__ = "Unsigned32"
_DDhcpFilterLogBufferSize_Object = MibScalar
dDhcpFilterLogBufferSize = _DDhcpFilterLogBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 133, 1, 1, 1),
    _DDhcpFilterLogBufferSize_Type()
)
dDhcpFilterLogBufferSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dDhcpFilterLogBufferSize.setStatus("current")


class _DDhcpFilterClearLogBuffer_Type(Integer32):
    """Custom type dDhcpFilterClearLogBuffer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("noOp", 2))
    )


_DDhcpFilterClearLogBuffer_Type.__name__ = "Integer32"
_DDhcpFilterClearLogBuffer_Object = MibScalar
dDhcpFilterClearLogBuffer = _DDhcpFilterClearLogBuffer_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 133, 1, 1, 2),
    _DDhcpFilterClearLogBuffer_Type()
)
dDhcpFilterClearLogBuffer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dDhcpFilterClearLogBuffer.setStatus("current")


class _DDhcpFilterGlobalNotifsEnabled_Type(TruthValue):
    """Custom type dDhcpFilterGlobalNotifsEnabled based on TruthValue"""
    defaultValue = 2


_DDhcpFilterGlobalNotifsEnabled_Type.__name__ = "TruthValue"
_DDhcpFilterGlobalNotifsEnabled_Object = MibScalar
dDhcpFilterGlobalNotifsEnabled = _DDhcpFilterGlobalNotifsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 133, 1, 1, 3),
    _DDhcpFilterGlobalNotifsEnabled_Type()
)
dDhcpFilterGlobalNotifsEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dDhcpFilterGlobalNotifsEnabled.setStatus("current")
_DDhcpFilterProfileObjects_ObjectIdentity = ObjectIdentity
dDhcpFilterProfileObjects = _DDhcpFilterProfileObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 133, 1, 2)
)
_DDhcpFilterProfileTable_Object = MibTable
dDhcpFilterProfileTable = _DDhcpFilterProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 133, 1, 2, 1)
)
if mibBuilder.loadTexts:
    dDhcpFilterProfileTable.setStatus("current")
_DDhcpFilterProfileEntry_Object = MibTableRow
dDhcpFilterProfileEntry = _DDhcpFilterProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 133, 1, 2, 1, 1)
)
dDhcpFilterProfileEntry.setIndexNames(
    (0, "DLINKSW-DHCP-FILTER-MIB", "dDhcpFilterProfileName"),
)
if mibBuilder.loadTexts:
    dDhcpFilterProfileEntry.setStatus("current")


class _DDhcpFilterProfileName_Type(DisplayString):
    """Custom type dDhcpFilterProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_DDhcpFilterProfileName_Type.__name__ = "DisplayString"
_DDhcpFilterProfileName_Object = MibTableColumn
dDhcpFilterProfileName = _DDhcpFilterProfileName_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 133, 1, 2, 1, 1, 1),
    _DDhcpFilterProfileName_Type()
)
dDhcpFilterProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dDhcpFilterProfileName.setStatus("current")
_DDhcpFilterProfileStatus_Type = RowStatus
_DDhcpFilterProfileStatus_Object = MibTableColumn
dDhcpFilterProfileStatus = _DDhcpFilterProfileStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 133, 1, 2, 1, 1, 99),
    _DDhcpFilterProfileStatus_Type()
)
dDhcpFilterProfileStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dDhcpFilterProfileStatus.setStatus("current")
_DDhcpFilterProfileClientTable_Object = MibTable
dDhcpFilterProfileClientTable = _DDhcpFilterProfileClientTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 133, 1, 2, 2)
)
if mibBuilder.loadTexts:
    dDhcpFilterProfileClientTable.setStatus("current")
_DDhcpFilterProfileClientEntry_Object = MibTableRow
dDhcpFilterProfileClientEntry = _DDhcpFilterProfileClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 133, 1, 2, 2, 1)
)
dDhcpFilterProfileClientEntry.setIndexNames(
    (0, "DLINKSW-DHCP-FILTER-MIB", "dDhcpFilterProfileName"),
    (0, "DLINKSW-DHCP-FILTER-MIB", "dDhcpFilterClientMacAddress"),
)
if mibBuilder.loadTexts:
    dDhcpFilterProfileClientEntry.setStatus("current")
_DDhcpFilterClientMacAddress_Type = MacAddress
_DDhcpFilterClientMacAddress_Object = MibTableColumn
dDhcpFilterClientMacAddress = _DDhcpFilterClientMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 133, 1, 2, 2, 1, 1),
    _DDhcpFilterClientMacAddress_Type()
)
dDhcpFilterClientMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dDhcpFilterClientMacAddress.setStatus("current")
_DDhcpFilterClientRowStatus_Type = RowStatus
_DDhcpFilterClientRowStatus_Object = MibTableColumn
dDhcpFilterClientRowStatus = _DDhcpFilterClientRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 133, 1, 2, 2, 1, 99),
    _DDhcpFilterClientRowStatus_Type()
)
dDhcpFilterClientRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dDhcpFilterClientRowStatus.setStatus("current")
_DDhcpFilterIfObjects_ObjectIdentity = ObjectIdentity
dDhcpFilterIfObjects = _DDhcpFilterIfObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 133, 1, 3)
)
_DDhcpFilterIfStateTable_Object = MibTable
dDhcpFilterIfStateTable = _DDhcpFilterIfStateTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 133, 1, 3, 1)
)
if mibBuilder.loadTexts:
    dDhcpFilterIfStateTable.setStatus("current")
_DDhcpFilterIfStateEntry_Object = MibTableRow
dDhcpFilterIfStateEntry = _DDhcpFilterIfStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 133, 1, 3, 1, 1)
)
dDhcpFilterIfStateEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dDhcpFilterIfStateEntry.setStatus("current")
_DDhcpFilterIfStateEnabled_Type = TruthValue
_DDhcpFilterIfStateEnabled_Object = MibTableColumn
dDhcpFilterIfStateEnabled = _DDhcpFilterIfStateEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 133, 1, 3, 1, 1, 1),
    _DDhcpFilterIfStateEnabled_Type()
)
dDhcpFilterIfStateEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dDhcpFilterIfStateEnabled.setStatus("current")
_DDhcpFilterIfTrustServerTable_Object = MibTable
dDhcpFilterIfTrustServerTable = _DDhcpFilterIfTrustServerTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 133, 1, 3, 2)
)
if mibBuilder.loadTexts:
    dDhcpFilterIfTrustServerTable.setStatus("current")
_DDhcpFilterIfTrustServerEntry_Object = MibTableRow
dDhcpFilterIfTrustServerEntry = _DDhcpFilterIfTrustServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 133, 1, 3, 2, 1)
)
dDhcpFilterIfTrustServerEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DLINKSW-DHCP-FILTER-MIB", "dDhcpFilterTrustServerIpAddress"),
)
if mibBuilder.loadTexts:
    dDhcpFilterIfTrustServerEntry.setStatus("current")
_DDhcpFilterTrustServerIpAddress_Type = IpAddress
_DDhcpFilterTrustServerIpAddress_Object = MibTableColumn
dDhcpFilterTrustServerIpAddress = _DDhcpFilterTrustServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 133, 1, 3, 2, 1, 1),
    _DDhcpFilterTrustServerIpAddress_Type()
)
dDhcpFilterTrustServerIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dDhcpFilterTrustServerIpAddress.setStatus("current")


class _DDhcpFilterTrustProfileName_Type(DisplayString):
    """Custom type dDhcpFilterTrustProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DDhcpFilterTrustProfileName_Type.__name__ = "DisplayString"
_DDhcpFilterTrustProfileName_Object = MibTableColumn
dDhcpFilterTrustProfileName = _DDhcpFilterTrustProfileName_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 133, 1, 3, 2, 1, 2),
    _DDhcpFilterTrustProfileName_Type()
)
dDhcpFilterTrustProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dDhcpFilterTrustProfileName.setStatus("current")
_DDhcpFilterTrustRowStatus_Type = RowStatus
_DDhcpFilterTrustRowStatus_Object = MibTableColumn
dDhcpFilterTrustRowStatus = _DDhcpFilterTrustRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 133, 1, 3, 2, 1, 99),
    _DDhcpFilterTrustRowStatus_Type()
)
dDhcpFilterTrustRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dDhcpFilterTrustRowStatus.setStatus("current")
_DDhcpFilterLogBufferObjects_ObjectIdentity = ObjectIdentity
dDhcpFilterLogBufferObjects = _DDhcpFilterLogBufferObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 133, 1, 4)
)
_DDhcpFilterLogBufferTable_Object = MibTable
dDhcpFilterLogBufferTable = _DDhcpFilterLogBufferTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 133, 1, 4, 1)
)
if mibBuilder.loadTexts:
    dDhcpFilterLogBufferTable.setStatus("current")
_DDhcpFilterLogBufferEntry_Object = MibTableRow
dDhcpFilterLogBufferEntry = _DDhcpFilterLogBufferEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 133, 1, 4, 1, 1)
)
dDhcpFilterLogBufferEntry.setIndexNames(
    (0, "DLINKSW-DHCP-FILTER-MIB", "dDhcpFilterLogBufferIndex"),
)
if mibBuilder.loadTexts:
    dDhcpFilterLogBufferEntry.setStatus("current")


class _DDhcpFilterLogBufferIndex_Type(Unsigned32):
    """Custom type dDhcpFilterLogBufferIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_DDhcpFilterLogBufferIndex_Type.__name__ = "Unsigned32"
_DDhcpFilterLogBufferIndex_Object = MibTableColumn
dDhcpFilterLogBufferIndex = _DDhcpFilterLogBufferIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 133, 1, 4, 1, 1, 1),
    _DDhcpFilterLogBufferIndex_Type()
)
dDhcpFilterLogBufferIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dDhcpFilterLogBufferIndex.setStatus("current")
_DDhcpFilterLogBufServerIpAddr_Type = IpAddress
_DDhcpFilterLogBufServerIpAddr_Object = MibTableColumn
dDhcpFilterLogBufServerIpAddr = _DDhcpFilterLogBufServerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 133, 1, 4, 1, 1, 2),
    _DDhcpFilterLogBufServerIpAddr_Type()
)
dDhcpFilterLogBufServerIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dDhcpFilterLogBufServerIpAddr.setStatus("current")
_DDhcpFilterLogBufClientMacAddr_Type = MacAddress
_DDhcpFilterLogBufClientMacAddr_Object = MibTableColumn
dDhcpFilterLogBufClientMacAddr = _DDhcpFilterLogBufClientMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 133, 1, 4, 1, 1, 3),
    _DDhcpFilterLogBufClientMacAddr_Type()
)
dDhcpFilterLogBufClientMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dDhcpFilterLogBufClientMacAddr.setStatus("current")
_DDhcpFilterLogBufferVlanId_Type = VlanId
_DDhcpFilterLogBufferVlanId_Object = MibTableColumn
dDhcpFilterLogBufferVlanId = _DDhcpFilterLogBufferVlanId_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 133, 1, 4, 1, 1, 4),
    _DDhcpFilterLogBufferVlanId_Type()
)
dDhcpFilterLogBufferVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dDhcpFilterLogBufferVlanId.setStatus("current")
_DDhcpFilterLogBufferOccurrence_Type = Unsigned32
_DDhcpFilterLogBufferOccurrence_Object = MibTableColumn
dDhcpFilterLogBufferOccurrence = _DDhcpFilterLogBufferOccurrence_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 133, 1, 4, 1, 1, 5),
    _DDhcpFilterLogBufferOccurrence_Type()
)
dDhcpFilterLogBufferOccurrence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dDhcpFilterLogBufferOccurrence.setStatus("current")
_DDhcpFilterLogBufferOccurTime_Type = DateAndTime
_DDhcpFilterLogBufferOccurTime_Object = MibTableColumn
dDhcpFilterLogBufferOccurTime = _DDhcpFilterLogBufferOccurTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 133, 1, 4, 1, 1, 6),
    _DDhcpFilterLogBufferOccurTime_Type()
)
dDhcpFilterLogBufferOccurTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dDhcpFilterLogBufferOccurTime.setStatus("current")
_DDhcpFilterMIBConformance_ObjectIdentity = ObjectIdentity
dDhcpFilterMIBConformance = _DDhcpFilterMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 133, 2)
)
_DDhcpFilterCompliances_ObjectIdentity = ObjectIdentity
dDhcpFilterCompliances = _DDhcpFilterCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 133, 2, 1)
)
_DDhcpFilterGroups_ObjectIdentity = ObjectIdentity
dDhcpFilterGroups = _DDhcpFilterGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 133, 2, 2)
)

# Managed Objects groups

dDhcpFilterTrustSrvCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 133, 2, 2, 1)
)
dDhcpFilterTrustSrvCfgGroup.setObjects(
      *(("DLINKSW-DHCP-FILTER-MIB", "dDhcpFilterProfileStatus"),
        ("DLINKSW-DHCP-FILTER-MIB", "dDhcpFilterClientMacAddress"),
        ("DLINKSW-DHCP-FILTER-MIB", "dDhcpFilterClientRowStatus"),
        ("DLINKSW-DHCP-FILTER-MIB", "dDhcpFilterTrustServerIpAddress"),
        ("DLINKSW-DHCP-FILTER-MIB", "dDhcpFilterTrustProfileName"),
        ("DLINKSW-DHCP-FILTER-MIB", "dDhcpFilterTrustRowStatus"))
)
if mibBuilder.loadTexts:
    dDhcpFilterTrustSrvCfgGroup.setStatus("current")

dDhcpFilterIfStateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 133, 2, 2, 2)
)
dDhcpFilterIfStateGroup.setObjects(
    ("DLINKSW-DHCP-FILTER-MIB", "dDhcpFilterIfStateEnabled")
)
if mibBuilder.loadTexts:
    dDhcpFilterIfStateGroup.setStatus("current")

dDhcpFilterLogGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 133, 2, 2, 3)
)
dDhcpFilterLogGroup.setObjects(
      *(("DLINKSW-DHCP-FILTER-MIB", "dDhcpFilterLogBufferSize"),
        ("DLINKSW-DHCP-FILTER-MIB", "dDhcpFilterClearLogBuffer"),
        ("DLINKSW-DHCP-FILTER-MIB", "dDhcpFilterLogBufServerIpAddr"),
        ("DLINKSW-DHCP-FILTER-MIB", "dDhcpFilterLogBufClientMacAddr"),
        ("DLINKSW-DHCP-FILTER-MIB", "dDhcpFilterLogBufferVlanId"),
        ("DLINKSW-DHCP-FILTER-MIB", "dDhcpFilterLogBufferOccurrence"),
        ("DLINKSW-DHCP-FILTER-MIB", "dDhcpFilterLogBufferOccurTime"))
)
if mibBuilder.loadTexts:
    dDhcpFilterLogGroup.setStatus("current")


# Notification objects

dDhcpFilterAttackDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 14, 133, 0, 1)
)
dDhcpFilterAttackDetected.setObjects(
      *(("DLINKSW-DHCP-FILTER-MIB", "dDhcpFilterLogBufServerIpAddr"),
        ("DLINKSW-DHCP-FILTER-MIB", "dDhcpFilterLogBufClientMacAddr"),
        ("DLINKSW-DHCP-FILTER-MIB", "dDhcpFilterLogBufferVlanId"),
        ("DLINKSW-DHCP-FILTER-MIB", "dDhcpFilterLogBufferOccurTime"))
)
if mibBuilder.loadTexts:
    dDhcpFilterAttackDetected.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

dDhcpFilterCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 171, 14, 133, 2, 1, 1)
)
dDhcpFilterCompliance.setObjects(
      *(("DLINKSW-DHCP-FILTER-MIB", "dDhcpFilterTrustSrvCfgGroup"),
        ("DLINKSW-DHCP-FILTER-MIB", "dDhcpFilterIfStateGroup"),
        ("DLINKSW-DHCP-FILTER-MIB", "dDhcpFilterLogGroup"))
)
if mibBuilder.loadTexts:
    dDhcpFilterCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLINKSW-DHCP-FILTER-MIB",
    **{"dlinkSwDhcpFilterMIB": dlinkSwDhcpFilterMIB,
       "dDhcpFilterMIBNotifications": dDhcpFilterMIBNotifications,
       "dDhcpFilterAttackDetected": dDhcpFilterAttackDetected,
       "dDhcpFilterMIBObjects": dDhcpFilterMIBObjects,
       "dDhcpFilterGlobalObjects": dDhcpFilterGlobalObjects,
       "dDhcpFilterLogBufferSize": dDhcpFilterLogBufferSize,
       "dDhcpFilterClearLogBuffer": dDhcpFilterClearLogBuffer,
       "dDhcpFilterGlobalNotifsEnabled": dDhcpFilterGlobalNotifsEnabled,
       "dDhcpFilterProfileObjects": dDhcpFilterProfileObjects,
       "dDhcpFilterProfileTable": dDhcpFilterProfileTable,
       "dDhcpFilterProfileEntry": dDhcpFilterProfileEntry,
       "dDhcpFilterProfileName": dDhcpFilterProfileName,
       "dDhcpFilterProfileStatus": dDhcpFilterProfileStatus,
       "dDhcpFilterProfileClientTable": dDhcpFilterProfileClientTable,
       "dDhcpFilterProfileClientEntry": dDhcpFilterProfileClientEntry,
       "dDhcpFilterClientMacAddress": dDhcpFilterClientMacAddress,
       "dDhcpFilterClientRowStatus": dDhcpFilterClientRowStatus,
       "dDhcpFilterIfObjects": dDhcpFilterIfObjects,
       "dDhcpFilterIfStateTable": dDhcpFilterIfStateTable,
       "dDhcpFilterIfStateEntry": dDhcpFilterIfStateEntry,
       "dDhcpFilterIfStateEnabled": dDhcpFilterIfStateEnabled,
       "dDhcpFilterIfTrustServerTable": dDhcpFilterIfTrustServerTable,
       "dDhcpFilterIfTrustServerEntry": dDhcpFilterIfTrustServerEntry,
       "dDhcpFilterTrustServerIpAddress": dDhcpFilterTrustServerIpAddress,
       "dDhcpFilterTrustProfileName": dDhcpFilterTrustProfileName,
       "dDhcpFilterTrustRowStatus": dDhcpFilterTrustRowStatus,
       "dDhcpFilterLogBufferObjects": dDhcpFilterLogBufferObjects,
       "dDhcpFilterLogBufferTable": dDhcpFilterLogBufferTable,
       "dDhcpFilterLogBufferEntry": dDhcpFilterLogBufferEntry,
       "dDhcpFilterLogBufferIndex": dDhcpFilterLogBufferIndex,
       "dDhcpFilterLogBufServerIpAddr": dDhcpFilterLogBufServerIpAddr,
       "dDhcpFilterLogBufClientMacAddr": dDhcpFilterLogBufClientMacAddr,
       "dDhcpFilterLogBufferVlanId": dDhcpFilterLogBufferVlanId,
       "dDhcpFilterLogBufferOccurrence": dDhcpFilterLogBufferOccurrence,
       "dDhcpFilterLogBufferOccurTime": dDhcpFilterLogBufferOccurTime,
       "dDhcpFilterMIBConformance": dDhcpFilterMIBConformance,
       "dDhcpFilterCompliances": dDhcpFilterCompliances,
       "dDhcpFilterCompliance": dDhcpFilterCompliance,
       "dDhcpFilterGroups": dDhcpFilterGroups,
       "dDhcpFilterTrustSrvCfgGroup": dDhcpFilterTrustSrvCfgGroup,
       "dDhcpFilterIfStateGroup": dDhcpFilterIfStateGroup,
       "dDhcpFilterLogGroup": dDhcpFilterLogGroup}
)
