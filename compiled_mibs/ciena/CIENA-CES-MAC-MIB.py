# SNMP MIB module (CIENA-CES-MAC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ciena\CIENA-CES-MAC-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:24:39 2025
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

(cienaCesConfig,
 cienaCesNotifications,
 cienaCesStatistics) = mibBuilder.importSymbols(
    "CIENA-SMI",
    "cienaCesConfig",
    "cienaCesNotifications",
    "cienaCesStatistics")

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
 MacAddress,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

cienaCesMacMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 26)
)
if mibBuilder.loadTexts:
    cienaCesMacMIB.setRevisions(
        ("2017-06-07 00:00",
         "2015-07-03 00:00",
         "2012-05-15 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CienaCesMacMIBObjects_ObjectIdentity = ObjectIdentity
cienaCesMacMIBObjects = _CienaCesMacMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 26, 1)
)
_CienaCesMacScan_ObjectIdentity = ObjectIdentity
cienaCesMacScan = _CienaCesMacScan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 26, 1, 1)
)
_CienaCesMacScanAttr_ObjectIdentity = ObjectIdentity
cienaCesMacScanAttr = _CienaCesMacScanAttr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 26, 1, 1, 1)
)


class _CienaCesMacScanAttrVs_Type(Integer32):
    """Custom type cienaCesMacScanAttrVs based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 65535),
    )


_CienaCesMacScanAttrVs_Type.__name__ = "Integer32"
_CienaCesMacScanAttrVs_Object = MibScalar
cienaCesMacScanAttrVs = _CienaCesMacScanAttrVs_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 26, 1, 1, 1, 1),
    _CienaCesMacScanAttrVs_Type()
)
cienaCesMacScanAttrVs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesMacScanAttrVs.setStatus("current")


class _CienaCesMacScanAttrRlan_Type(Integer32):
    """Custom type cienaCesMacScanAttrRlan based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 65535),
    )


_CienaCesMacScanAttrRlan_Type.__name__ = "Integer32"
_CienaCesMacScanAttrRlan_Object = MibScalar
cienaCesMacScanAttrRlan = _CienaCesMacScanAttrRlan_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 26, 1, 1, 1, 2),
    _CienaCesMacScanAttrRlan_Type()
)
cienaCesMacScanAttrRlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesMacScanAttrRlan.setStatus("current")


class _CienaCesMacScanAttrMac_Type(MacAddress):
    """Custom type cienaCesMacScanAttrMac based on MacAddress"""
    defaultHexValue = "000000000000"


_CienaCesMacScanAttrMac_Type.__name__ = "MacAddress"
_CienaCesMacScanAttrMac_Object = MibScalar
cienaCesMacScanAttrMac = _CienaCesMacScanAttrMac_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 26, 1, 1, 1, 3),
    _CienaCesMacScanAttrMac_Type()
)
cienaCesMacScanAttrMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesMacScanAttrMac.setStatus("current")


class _CienaCesMacScanAttrMask_Type(MacAddress):
    """Custom type cienaCesMacScanAttrMask based on MacAddress"""
    defaultHexValue = "000000000000"


_CienaCesMacScanAttrMask_Type.__name__ = "MacAddress"
_CienaCesMacScanAttrMask_Object = MibScalar
cienaCesMacScanAttrMask = _CienaCesMacScanAttrMask_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 26, 1, 1, 1, 4),
    _CienaCesMacScanAttrMask_Type()
)
cienaCesMacScanAttrMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesMacScanAttrMask.setStatus("current")
_CienaCesMacScanTable_Object = MibTable
cienaCesMacScanTable = _CienaCesMacScanTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 26, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cienaCesMacScanTable.setStatus("current")
_CienaCesMacScanEntry_Object = MibTableRow
cienaCesMacScanEntry = _CienaCesMacScanEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 26, 1, 1, 2, 1)
)
cienaCesMacScanEntry.setIndexNames(
    (0, "CIENA-CES-MAC-MIB", "cienaCesMacScanVsIndex"),
    (0, "CIENA-CES-MAC-MIB", "cienaCesMacScanRlanIndex"),
    (0, "CIENA-CES-MAC-MIB", "cienaCesMacScanMacIndex"),
)
if mibBuilder.loadTexts:
    cienaCesMacScanEntry.setStatus("current")
_CienaCesMacScanVsIndex_Type = Unsigned32
_CienaCesMacScanVsIndex_Object = MibTableColumn
cienaCesMacScanVsIndex = _CienaCesMacScanVsIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 26, 1, 1, 2, 1, 1),
    _CienaCesMacScanVsIndex_Type()
)
cienaCesMacScanVsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesMacScanVsIndex.setStatus("current")
_CienaCesMacScanRlanIndex_Type = Unsigned32
_CienaCesMacScanRlanIndex_Object = MibTableColumn
cienaCesMacScanRlanIndex = _CienaCesMacScanRlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 26, 1, 1, 2, 1, 2),
    _CienaCesMacScanRlanIndex_Type()
)
cienaCesMacScanRlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesMacScanRlanIndex.setStatus("current")
_CienaCesMacScanMacIndex_Type = MacAddress
_CienaCesMacScanMacIndex_Object = MibTableColumn
cienaCesMacScanMacIndex = _CienaCesMacScanMacIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 26, 1, 1, 2, 1, 3),
    _CienaCesMacScanMacIndex_Type()
)
cienaCesMacScanMacIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesMacScanMacIndex.setStatus("current")
_CienaCesMacScanVsId_Type = Unsigned32
_CienaCesMacScanVsId_Object = MibTableColumn
cienaCesMacScanVsId = _CienaCesMacScanVsId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 26, 1, 1, 2, 1, 4),
    _CienaCesMacScanVsId_Type()
)
cienaCesMacScanVsId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMacScanVsId.setStatus("current")
_CienaCesMacScanRlanId_Type = Unsigned32
_CienaCesMacScanRlanId_Object = MibTableColumn
cienaCesMacScanRlanId = _CienaCesMacScanRlanId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 26, 1, 1, 2, 1, 5),
    _CienaCesMacScanRlanId_Type()
)
cienaCesMacScanRlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesMacScanRlanId.setStatus("current")
_CienaCesMacScanMacAddr_Type = DisplayString
_CienaCesMacScanMacAddr_Object = MibTableColumn
cienaCesMacScanMacAddr = _CienaCesMacScanMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 26, 1, 1, 2, 1, 6),
    _CienaCesMacScanMacAddr_Type()
)
cienaCesMacScanMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMacScanMacAddr.setStatus("current")


class _CienaCesMacScanLiType_Type(Integer32):
    """Custom type cienaCesMacScanLiType based on Integer32"""
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
              21,
              22)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("port", 2),
          ("tunnelEncapPbt", 3),
          ("tunnelDecapPbt", 4),
          ("tunnelGroupPbt", 5),
          ("transitPbt", 6),
          ("tunnelEncapMpls", 7),
          ("tunnelDecapMpls", 8),
          ("transitMpls", 9),
          ("subPort", 10),
          ("qosFlow", 11),
          ("accessFlow", 12),
          ("servicePbt", 13),
          ("servicePbb", 14),
          ("serviceMplsMesh", 15),
          ("cpuInterface", 16),
          ("cpuSubInterface", 17),
          ("tunnelGroupMpls", 18),
          ("vcMpls", 19),
          ("lspEncapMpls", 20),
          ("lspDecapMpls", 21),
          ("l3Interface", 22))
    )


_CienaCesMacScanLiType_Type.__name__ = "Integer32"
_CienaCesMacScanLiType_Object = MibTableColumn
cienaCesMacScanLiType = _CienaCesMacScanLiType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 26, 1, 1, 2, 1, 7),
    _CienaCesMacScanLiType_Type()
)
cienaCesMacScanLiType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMacScanLiType.setStatus("current")
_CienaCesMacScanLiIndex_Type = Unsigned32
_CienaCesMacScanLiIndex_Object = MibTableColumn
cienaCesMacScanLiIndex = _CienaCesMacScanLiIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 26, 1, 1, 2, 1, 8),
    _CienaCesMacScanLiIndex_Type()
)
cienaCesMacScanLiIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMacScanLiIndex.setStatus("current")
_CienaCesMacScanPortBayIndex_Type = Unsigned32
_CienaCesMacScanPortBayIndex_Object = MibTableColumn
cienaCesMacScanPortBayIndex = _CienaCesMacScanPortBayIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 26, 1, 1, 2, 1, 9),
    _CienaCesMacScanPortBayIndex_Type()
)
cienaCesMacScanPortBayIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMacScanPortBayIndex.setStatus("current")
_CienaCesMacScanPortShelfIndex_Type = Unsigned32
_CienaCesMacScanPortShelfIndex_Object = MibTableColumn
cienaCesMacScanPortShelfIndex = _CienaCesMacScanPortShelfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 26, 1, 1, 2, 1, 10),
    _CienaCesMacScanPortShelfIndex_Type()
)
cienaCesMacScanPortShelfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMacScanPortShelfIndex.setStatus("current")
_CienaCesMacScanPortSlotIndex_Type = Unsigned32
_CienaCesMacScanPortSlotIndex_Object = MibTableColumn
cienaCesMacScanPortSlotIndex = _CienaCesMacScanPortSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 26, 1, 1, 2, 1, 11),
    _CienaCesMacScanPortSlotIndex_Type()
)
cienaCesMacScanPortSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMacScanPortSlotIndex.setStatus("current")
_CienaCesMacScanPortPortId_Type = Unsigned32
_CienaCesMacScanPortPortId_Object = MibTableColumn
cienaCesMacScanPortPortId = _CienaCesMacScanPortPortId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 26, 1, 1, 2, 1, 12),
    _CienaCesMacScanPortPortId_Type()
)
cienaCesMacScanPortPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMacScanPortPortId.setStatus("current")


class _CienaCesMacScanMacType_Type(Integer32):
    """Custom type cienaCesMacScanMacType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 1),
          ("static", 2))
    )


_CienaCesMacScanMacType_Type.__name__ = "Integer32"
_CienaCesMacScanMacType_Object = MibTableColumn
cienaCesMacScanMacType = _CienaCesMacScanMacType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 26, 1, 1, 2, 1, 13),
    _CienaCesMacScanMacType_Type()
)
cienaCesMacScanMacType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMacScanMacType.setStatus("current")
_CienaCesMacScanPortChannelId_Type = Unsigned32
_CienaCesMacScanPortChannelId_Object = MibTableColumn
cienaCesMacScanPortChannelId = _CienaCesMacScanPortChannelId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 26, 1, 1, 2, 1, 14),
    _CienaCesMacScanPortChannelId_Type()
)
cienaCesMacScanPortChannelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMacScanPortChannelId.setStatus("current")
_CienaCesMacMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
cienaCesMacMIBNotificationPrefix = _CienaCesMacMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 26, 2)
)
_CienaCesMacMIBNotifications_ObjectIdentity = ObjectIdentity
cienaCesMacMIBNotifications = _CienaCesMacMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 26, 2, 0)
)
_CienaCesMacMIBConformance_ObjectIdentity = ObjectIdentity
cienaCesMacMIBConformance = _CienaCesMacMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 26, 3)
)
_CienaCesMacMIBCompliances_ObjectIdentity = ObjectIdentity
cienaCesMacMIBCompliances = _CienaCesMacMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 26, 3, 1)
)
_CienaCesMacMIBGroups_ObjectIdentity = ObjectIdentity
cienaCesMacMIBGroups = _CienaCesMacMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 26, 3, 2)
)

# Managed Objects groups

cienaCesMacScanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 26, 3, 2, 1)
)
cienaCesMacScanGroup.setObjects(
      *(("CIENA-CES-MAC-MIB", "cienaCesMacScanAttrVs"),
        ("CIENA-CES-MAC-MIB", "cienaCesMacScanAttrRlan"),
        ("CIENA-CES-MAC-MIB", "cienaCesMacScanAttrMac"),
        ("CIENA-CES-MAC-MIB", "cienaCesMacScanAttrMask"),
        ("CIENA-CES-MAC-MIB", "cienaCesMacScanVsId"),
        ("CIENA-CES-MAC-MIB", "cienaCesMacScanMacAddr"),
        ("CIENA-CES-MAC-MIB", "cienaCesMacScanLiType"),
        ("CIENA-CES-MAC-MIB", "cienaCesMacScanLiIndex"),
        ("CIENA-CES-MAC-MIB", "cienaCesMacScanPortBayIndex"),
        ("CIENA-CES-MAC-MIB", "cienaCesMacScanPortShelfIndex"),
        ("CIENA-CES-MAC-MIB", "cienaCesMacScanPortSlotIndex"),
        ("CIENA-CES-MAC-MIB", "cienaCesMacScanPortPortId"),
        ("CIENA-CES-MAC-MIB", "cienaCesMacScanMacType"),
        ("CIENA-CES-MAC-MIB", "cienaCesMacScanPortChannelId"))
)
if mibBuilder.loadTexts:
    cienaCesMacScanGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CIENA-CES-MAC-MIB",
    **{"cienaCesMacMIB": cienaCesMacMIB,
       "cienaCesMacMIBObjects": cienaCesMacMIBObjects,
       "cienaCesMacScan": cienaCesMacScan,
       "cienaCesMacScanAttr": cienaCesMacScanAttr,
       "cienaCesMacScanAttrVs": cienaCesMacScanAttrVs,
       "cienaCesMacScanAttrRlan": cienaCesMacScanAttrRlan,
       "cienaCesMacScanAttrMac": cienaCesMacScanAttrMac,
       "cienaCesMacScanAttrMask": cienaCesMacScanAttrMask,
       "cienaCesMacScanTable": cienaCesMacScanTable,
       "cienaCesMacScanEntry": cienaCesMacScanEntry,
       "cienaCesMacScanVsIndex": cienaCesMacScanVsIndex,
       "cienaCesMacScanRlanIndex": cienaCesMacScanRlanIndex,
       "cienaCesMacScanMacIndex": cienaCesMacScanMacIndex,
       "cienaCesMacScanVsId": cienaCesMacScanVsId,
       "cienaCesMacScanRlanId": cienaCesMacScanRlanId,
       "cienaCesMacScanMacAddr": cienaCesMacScanMacAddr,
       "cienaCesMacScanLiType": cienaCesMacScanLiType,
       "cienaCesMacScanLiIndex": cienaCesMacScanLiIndex,
       "cienaCesMacScanPortBayIndex": cienaCesMacScanPortBayIndex,
       "cienaCesMacScanPortShelfIndex": cienaCesMacScanPortShelfIndex,
       "cienaCesMacScanPortSlotIndex": cienaCesMacScanPortSlotIndex,
       "cienaCesMacScanPortPortId": cienaCesMacScanPortPortId,
       "cienaCesMacScanMacType": cienaCesMacScanMacType,
       "cienaCesMacScanPortChannelId": cienaCesMacScanPortChannelId,
       "cienaCesMacMIBNotificationPrefix": cienaCesMacMIBNotificationPrefix,
       "cienaCesMacMIBNotifications": cienaCesMacMIBNotifications,
       "cienaCesMacMIBConformance": cienaCesMacMIBConformance,
       "cienaCesMacMIBCompliances": cienaCesMacMIBCompliances,
       "cienaCesMacMIBGroups": cienaCesMacMIBGroups,
       "cienaCesMacScanGroup": cienaCesMacScanGroup}
)
