# SNMP MIB module (ATKK-WLAN-ACCESS) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\awplus\ATKK-WLAN-ACCESS-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:20:43 2025
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

(wirelessLanmMIB,
 wirelesslan) = mibBuilder.importSymbols(
    "AT-SMI-MIB",
    "wirelessLanmMIB",
    "wirelesslan")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

atkkWlanAccess = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 6)
)
if mibBuilder.loadTexts:
    atkkWlanAccess.setRevisions(
        ("2016-05-25 00:00",
         "2016-03-23 00:00",
         "2015-06-17 00:00",
         "2015-05-11 00:00",
         "2014-09-30 00:00",
         "2013-11-22 00:00",
         "2012-08-13 00:00",
         "2012-07-09 00:00",
         "2012-06-06 00:00",
         "2012-01-11 00:00",
         "2011-04-08 00:00",
         "2010-08-20 00:00",
         "2009-07-28 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class SsidString(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )



class UserIdString(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class TrapHostString(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )



class CommunityString(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )



class TrapString(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )



class ChannelString(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )



# MIB Managed Objects in the order of their OIDs

_Tq2403_ObjectIdentity = ObjectIdentity
tq2403 = _Tq2403_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 13, 13)
)
_Tq2450_ObjectIdentity = ObjectIdentity
tq2450 = _Tq2450_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 13, 19)
)
_Tq2403ex_ObjectIdentity = ObjectIdentity
tq2403ex = _Tq2403ex_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 13, 20)
)
_Tq3600_ObjectIdentity = ObjectIdentity
tq3600 = _Tq3600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 13, 22)
)
_Tq3200_ObjectIdentity = ObjectIdentity
tq3200 = _Tq3200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 13, 24)
)
_Tq3400_ObjectIdentity = ObjectIdentity
tq3400 = _Tq3400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 13, 25)
)
_Tq4400_ObjectIdentity = ObjectIdentity
tq4400 = _Tq4400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 13, 26)
)
_Tq4600_ObjectIdentity = ObjectIdentity
tq4600 = _Tq4600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 13, 27)
)
_Tq4400e_ObjectIdentity = ObjectIdentity
tq4400e = _Tq4400e_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 13, 34)
)
_AtkkWiAcVersion_Type = Integer32
_AtkkWiAcVersion_Object = MibScalar
atkkWiAcVersion = _AtkkWiAcVersion_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 1),
    _AtkkWiAcVersion_Type()
)
atkkWiAcVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atkkWiAcVersion.setStatus("current")
_AtkkWiAcClients_ObjectIdentity = ObjectIdentity
atkkWiAcClients = _AtkkWiAcClients_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 2)
)
if mibBuilder.loadTexts:
    atkkWiAcClients.setStatus("current")
_AtkkWiAcClientTable_Object = MibTable
atkkWiAcClientTable = _AtkkWiAcClientTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 2, 1)
)
if mibBuilder.loadTexts:
    atkkWiAcClientTable.setStatus("current")
_AtkkWiAcClientEntry_Object = MibTableRow
atkkWiAcClientEntry = _AtkkWiAcClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 2, 1, 1)
)
atkkWiAcClientEntry.setIndexNames(
    (0, "ATKK-WLAN-ACCESS", "atkkWiAcClientAddress"),
)
if mibBuilder.loadTexts:
    atkkWiAcClientEntry.setStatus("current")
_AtkkWiAcClientAddress_Type = MacAddress
_AtkkWiAcClientAddress_Object = MibTableColumn
atkkWiAcClientAddress = _AtkkWiAcClientAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 2, 1, 1, 1),
    _AtkkWiAcClientAddress_Type()
)
atkkWiAcClientAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atkkWiAcClientAddress.setStatus("current")
_AtkkWiAcClientSSID_Type = SsidString
_AtkkWiAcClientSSID_Object = MibTableColumn
atkkWiAcClientSSID = _AtkkWiAcClientSSID_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 2, 1, 1, 2),
    _AtkkWiAcClientSSID_Type()
)
atkkWiAcClientSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atkkWiAcClientSSID.setStatus("current")


class _AtkkWiAcClient80211Spec_Type(Integer32):
    """Custom type atkkWiAcClient80211Spec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("dot11b", 2),
          ("dot11g", 3),
          ("dot11a", 4),
          ("dot11ng", 5),
          ("dot11na", 6),
          ("dot11ac", 7))
    )


_AtkkWiAcClient80211Spec_Type.__name__ = "Integer32"
_AtkkWiAcClient80211Spec_Object = MibTableColumn
atkkWiAcClient80211Spec = _AtkkWiAcClient80211Spec_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 2, 1, 1, 3),
    _AtkkWiAcClient80211Spec_Type()
)
atkkWiAcClient80211Spec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atkkWiAcClient80211Spec.setStatus("current")
_AtkkWiAcClientChannel_Type = Integer32
_AtkkWiAcClientChannel_Object = MibTableColumn
atkkWiAcClientChannel = _AtkkWiAcClientChannel_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 2, 1, 1, 4),
    _AtkkWiAcClientChannel_Type()
)
atkkWiAcClientChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atkkWiAcClientChannel.setStatus("current")
_AtkkWiAcClientAge_Type = Counter32
_AtkkWiAcClientAge_Object = MibTableColumn
atkkWiAcClientAge = _AtkkWiAcClientAge_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 2, 1, 1, 5),
    _AtkkWiAcClientAge_Type()
)
atkkWiAcClientAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atkkWiAcClientAge.setStatus("current")
_AtkkWiAcClientUserID_Type = UserIdString
_AtkkWiAcClientUserID_Object = MibTableColumn
atkkWiAcClientUserID = _AtkkWiAcClientUserID_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 2, 1, 1, 6),
    _AtkkWiAcClientUserID_Type()
)
atkkWiAcClientUserID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atkkWiAcClientUserID.setStatus("current")
_AtkkWiAcAPs_ObjectIdentity = ObjectIdentity
atkkWiAcAPs = _AtkkWiAcAPs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 3)
)
if mibBuilder.loadTexts:
    atkkWiAcAPs.setStatus("current")
_AtkkWiAcAPTable_Object = MibTable
atkkWiAcAPTable = _AtkkWiAcAPTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 3, 1)
)
if mibBuilder.loadTexts:
    atkkWiAcAPTable.setStatus("current")
_AtkkWiAcAPEntry_Object = MibTableRow
atkkWiAcAPEntry = _AtkkWiAcAPEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 3, 1, 1)
)
atkkWiAcAPEntry.setIndexNames(
    (0, "ATKK-WLAN-ACCESS", "atkkWiAcAPAddress"),
)
if mibBuilder.loadTexts:
    atkkWiAcAPEntry.setStatus("current")
_AtkkWiAcAPAddress_Type = MacAddress
_AtkkWiAcAPAddress_Object = MibTableColumn
atkkWiAcAPAddress = _AtkkWiAcAPAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 3, 1, 1, 1),
    _AtkkWiAcAPAddress_Type()
)
atkkWiAcAPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atkkWiAcAPAddress.setStatus("current")
_AtkkWiAcAPSSID_Type = SsidString
_AtkkWiAcAPSSID_Object = MibTableColumn
atkkWiAcAPSSID = _AtkkWiAcAPSSID_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 3, 1, 1, 2),
    _AtkkWiAcAPSSID_Type()
)
atkkWiAcAPSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atkkWiAcAPSSID.setStatus("current")


class _AtkkWiAcAP80211Spec_Type(Integer32):
    """Custom type atkkWiAcAP80211Spec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("dot11b", 2),
          ("dot11g", 3),
          ("dot11a", 4),
          ("dot11ng", 5),
          ("dot11na", 6),
          ("dot11ac", 7))
    )


_AtkkWiAcAP80211Spec_Type.__name__ = "Integer32"
_AtkkWiAcAP80211Spec_Object = MibTableColumn
atkkWiAcAP80211Spec = _AtkkWiAcAP80211Spec_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 3, 1, 1, 3),
    _AtkkWiAcAP80211Spec_Type()
)
atkkWiAcAP80211Spec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atkkWiAcAP80211Spec.setStatus("current")
_AtkkWiAcAPChannel_Type = Integer32
_AtkkWiAcAPChannel_Object = MibTableColumn
atkkWiAcAPChannel = _AtkkWiAcAPChannel_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 3, 1, 1, 4),
    _AtkkWiAcAPChannel_Type()
)
atkkWiAcAPChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atkkWiAcAPChannel.setStatus("current")
_AtkkWiAcAPRSSI_Type = Integer32
_AtkkWiAcAPRSSI_Object = MibTableColumn
atkkWiAcAPRSSI = _AtkkWiAcAPRSSI_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 3, 1, 1, 5),
    _AtkkWiAcAPRSSI_Type()
)
atkkWiAcAPRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atkkWiAcAPRSSI.setStatus("current")
_AtkkWiAcAPRadarDetected_Type = TrapString
_AtkkWiAcAPRadarDetected_Object = MibTableColumn
atkkWiAcAPRadarDetected = _AtkkWiAcAPRadarDetected_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 3, 1, 1, 6),
    _AtkkWiAcAPRadarDetected_Type()
)
atkkWiAcAPRadarDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atkkWiAcAPRadarDetected.setStatus("current")
_AtkkWiAcAPChannels_Type = ChannelString
_AtkkWiAcAPChannels_Object = MibTableColumn
atkkWiAcAPChannels = _AtkkWiAcAPChannels_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 3, 1, 1, 7),
    _AtkkWiAcAPChannels_Type()
)
atkkWiAcAPChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atkkWiAcAPChannels.setStatus("current")


class _AtkkWiAcAPDetectConfig_Type(Integer32):
    """Custom type atkkWiAcAPDetectConfig based on Integer32"""
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


_AtkkWiAcAPDetectConfig_Type.__name__ = "Integer32"
_AtkkWiAcAPDetectConfig_Object = MibScalar
atkkWiAcAPDetectConfig = _AtkkWiAcAPDetectConfig_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 3, 2),
    _AtkkWiAcAPDetectConfig_Type()
)
atkkWiAcAPDetectConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atkkWiAcAPDetectConfig.setStatus("current")


class _AtkkWiAcAPDetectConfig2_Type(Integer32):
    """Custom type atkkWiAcAPDetectConfig2 based on Integer32"""
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


_AtkkWiAcAPDetectConfig2_Type.__name__ = "Integer32"
_AtkkWiAcAPDetectConfig2_Object = MibScalar
atkkWiAcAPDetectConfig2 = _AtkkWiAcAPDetectConfig2_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 3, 3),
    _AtkkWiAcAPDetectConfig2_Type()
)
atkkWiAcAPDetectConfig2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atkkWiAcAPDetectConfig2.setStatus("current")
_AtkkWiAcMacACL_ObjectIdentity = ObjectIdentity
atkkWiAcMacACL = _AtkkWiAcMacACL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 4)
)
if mibBuilder.loadTexts:
    atkkWiAcMacACL.setStatus("current")
_AtkkWiAcMacACLTable_Object = MibTable
atkkWiAcMacACLTable = _AtkkWiAcMacACLTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 4, 1)
)
if mibBuilder.loadTexts:
    atkkWiAcMacACLTable.setStatus("current")
_AtkkWiAcMacACLEntry_Object = MibTableRow
atkkWiAcMacACLEntry = _AtkkWiAcMacACLEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 4, 1, 1)
)
atkkWiAcMacACLEntry.setIndexNames(
    (0, "ATKK-WLAN-ACCESS", "atkkWiAcMacACLAddress"),
)
if mibBuilder.loadTexts:
    atkkWiAcMacACLEntry.setStatus("current")
_AtkkWiAcMacACLAddress_Type = MacAddress
_AtkkWiAcMacACLAddress_Object = MibTableColumn
atkkWiAcMacACLAddress = _AtkkWiAcMacACLAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 4, 1, 1, 1),
    _AtkkWiAcMacACLAddress_Type()
)
atkkWiAcMacACLAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atkkWiAcMacACLAddress.setStatus("current")


class _AtkkWiAcMacACLModeConfig_Type(Integer32):
    """Custom type atkkWiAcMacACLModeConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 1),
          ("accept", 2))
    )


_AtkkWiAcMacACLModeConfig_Type.__name__ = "Integer32"
_AtkkWiAcMacACLModeConfig_Object = MibScalar
atkkWiAcMacACLModeConfig = _AtkkWiAcMacACLModeConfig_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 4, 2),
    _AtkkWiAcMacACLModeConfig_Type()
)
atkkWiAcMacACLModeConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atkkWiAcMacACLModeConfig.setStatus("current")
_AtkkWiAcNotification_ObjectIdentity = ObjectIdentity
atkkWiAcNotification = _AtkkWiAcNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 5)
)
_AtkkWiAcNotificationObjects_ObjectIdentity = ObjectIdentity
atkkWiAcNotificationObjects = _AtkkWiAcNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 5, 0)
)
_AtkkWiAcApInfo_ObjectIdentity = ObjectIdentity
atkkWiAcApInfo = _AtkkWiAcApInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 6)
)
if mibBuilder.loadTexts:
    atkkWiAcApInfo.setStatus("current")
_AtkkWiAcApInfoTrapTable_Object = MibTable
atkkWiAcApInfoTrapTable = _AtkkWiAcApInfoTrapTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 6, 1)
)
if mibBuilder.loadTexts:
    atkkWiAcApInfoTrapTable.setStatus("current")
_AtkkWiAcApInfoTrapEntry_Object = MibTableRow
atkkWiAcApInfoTrapEntry = _AtkkWiAcApInfoTrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 6, 1, 1)
)
atkkWiAcApInfoTrapEntry.setIndexNames(
    (0, "ATKK-WLAN-ACCESS", "atkkWiAcApTrapHost"),
)
if mibBuilder.loadTexts:
    atkkWiAcApInfoTrapEntry.setStatus("current")
_AtkkWiAcApTrapHost_Type = TrapHostString
_AtkkWiAcApTrapHost_Object = MibTableColumn
atkkWiAcApTrapHost = _AtkkWiAcApTrapHost_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 6, 1, 1, 1),
    _AtkkWiAcApTrapHost_Type()
)
atkkWiAcApTrapHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atkkWiAcApTrapHost.setStatus("current")
_AtkkWiAcApTrapCommunity_Type = CommunityString
_AtkkWiAcApTrapCommunity_Object = MibTableColumn
atkkWiAcApTrapCommunity = _AtkkWiAcApTrapCommunity_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 6, 1, 1, 2),
    _AtkkWiAcApTrapCommunity_Type()
)
atkkWiAcApTrapCommunity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atkkWiAcApTrapCommunity.setStatus("current")


class _AtkkWiAcApTrapColdStartConfig_Type(Integer32):
    """Custom type atkkWiAcApTrapColdStartConfig based on Integer32"""
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


_AtkkWiAcApTrapColdStartConfig_Type.__name__ = "Integer32"
_AtkkWiAcApTrapColdStartConfig_Object = MibTableColumn
atkkWiAcApTrapColdStartConfig = _AtkkWiAcApTrapColdStartConfig_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 6, 1, 1, 3),
    _AtkkWiAcApTrapColdStartConfig_Type()
)
atkkWiAcApTrapColdStartConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atkkWiAcApTrapColdStartConfig.setStatus("current")


class _AtkkWiAcApTrapLinkConfig_Type(Integer32):
    """Custom type atkkWiAcApTrapLinkConfig based on Integer32"""
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


_AtkkWiAcApTrapLinkConfig_Type.__name__ = "Integer32"
_AtkkWiAcApTrapLinkConfig_Object = MibTableColumn
atkkWiAcApTrapLinkConfig = _AtkkWiAcApTrapLinkConfig_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 6, 1, 1, 4),
    _AtkkWiAcApTrapLinkConfig_Type()
)
atkkWiAcApTrapLinkConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atkkWiAcApTrapLinkConfig.setStatus("current")


class _AtkkWiAcApTrapAuthenticationConfig_Type(Integer32):
    """Custom type atkkWiAcApTrapAuthenticationConfig based on Integer32"""
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


_AtkkWiAcApTrapAuthenticationConfig_Type.__name__ = "Integer32"
_AtkkWiAcApTrapAuthenticationConfig_Object = MibTableColumn
atkkWiAcApTrapAuthenticationConfig = _AtkkWiAcApTrapAuthenticationConfig_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 6, 1, 1, 5),
    _AtkkWiAcApTrapAuthenticationConfig_Type()
)
atkkWiAcApTrapAuthenticationConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atkkWiAcApTrapAuthenticationConfig.setStatus("current")


class _AtkkWiAcApTrapAssociationConfig_Type(Integer32):
    """Custom type atkkWiAcApTrapAssociationConfig based on Integer32"""
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


_AtkkWiAcApTrapAssociationConfig_Type.__name__ = "Integer32"
_AtkkWiAcApTrapAssociationConfig_Object = MibTableColumn
atkkWiAcApTrapAssociationConfig = _AtkkWiAcApTrapAssociationConfig_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 6, 1, 1, 6),
    _AtkkWiAcApTrapAssociationConfig_Type()
)
atkkWiAcApTrapAssociationConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atkkWiAcApTrapAssociationConfig.setStatus("current")


class _AtkkWiAcApTrapUnknownApConfig_Type(Integer32):
    """Custom type atkkWiAcApTrapUnknownApConfig based on Integer32"""
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


_AtkkWiAcApTrapUnknownApConfig_Type.__name__ = "Integer32"
_AtkkWiAcApTrapUnknownApConfig_Object = MibTableColumn
atkkWiAcApTrapUnknownApConfig = _AtkkWiAcApTrapUnknownApConfig_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 6, 1, 1, 7),
    _AtkkWiAcApTrapUnknownApConfig_Type()
)
atkkWiAcApTrapUnknownApConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atkkWiAcApTrapUnknownApConfig.setStatus("current")


class _AtkkWiAcApTrapFilteredStaConfig_Type(Integer32):
    """Custom type atkkWiAcApTrapFilteredStaConfig based on Integer32"""
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


_AtkkWiAcApTrapFilteredStaConfig_Type.__name__ = "Integer32"
_AtkkWiAcApTrapFilteredStaConfig_Object = MibTableColumn
atkkWiAcApTrapFilteredStaConfig = _AtkkWiAcApTrapFilteredStaConfig_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 6, 1, 1, 8),
    _AtkkWiAcApTrapFilteredStaConfig_Type()
)
atkkWiAcApTrapFilteredStaConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atkkWiAcApTrapFilteredStaConfig.setStatus("current")


class _AtkkWiAcApTrapRadiusAuthSuccessConfig_Type(Integer32):
    """Custom type atkkWiAcApTrapRadiusAuthSuccessConfig based on Integer32"""
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


_AtkkWiAcApTrapRadiusAuthSuccessConfig_Type.__name__ = "Integer32"
_AtkkWiAcApTrapRadiusAuthSuccessConfig_Object = MibTableColumn
atkkWiAcApTrapRadiusAuthSuccessConfig = _AtkkWiAcApTrapRadiusAuthSuccessConfig_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 6, 1, 1, 9),
    _AtkkWiAcApTrapRadiusAuthSuccessConfig_Type()
)
atkkWiAcApTrapRadiusAuthSuccessConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atkkWiAcApTrapRadiusAuthSuccessConfig.setStatus("current")


class _AtkkWiAcApTrapRadiusAuthFailConfig_Type(Integer32):
    """Custom type atkkWiAcApTrapRadiusAuthFailConfig based on Integer32"""
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


_AtkkWiAcApTrapRadiusAuthFailConfig_Type.__name__ = "Integer32"
_AtkkWiAcApTrapRadiusAuthFailConfig_Object = MibTableColumn
atkkWiAcApTrapRadiusAuthFailConfig = _AtkkWiAcApTrapRadiusAuthFailConfig_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 6, 1, 1, 10),
    _AtkkWiAcApTrapRadiusAuthFailConfig_Type()
)
atkkWiAcApTrapRadiusAuthFailConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atkkWiAcApTrapRadiusAuthFailConfig.setStatus("current")


class _AtkkWiAcApTrapDfsDetectedConfig_Type(Integer32):
    """Custom type atkkWiAcApTrapDfsDetectedConfig based on Integer32"""
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


_AtkkWiAcApTrapDfsDetectedConfig_Type.__name__ = "Integer32"
_AtkkWiAcApTrapDfsDetectedConfig_Object = MibTableColumn
atkkWiAcApTrapDfsDetectedConfig = _AtkkWiAcApTrapDfsDetectedConfig_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 6, 1, 1, 11),
    _AtkkWiAcApTrapDfsDetectedConfig_Type()
)
atkkWiAcApTrapDfsDetectedConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atkkWiAcApTrapDfsDetectedConfig.setStatus("current")

# Managed Objects groups


# Notification objects

atkkWiAcAssociated = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 5, 0, 1)
)
atkkWiAcAssociated.setObjects(
      *(("ATKK-WLAN-ACCESS", "atkkWiAcClientAddress"),
        ("ATKK-WLAN-ACCESS", "atkkWiAcClientSSID"),
        ("ATKK-WLAN-ACCESS", "atkkWiAcClient80211Spec"),
        ("ATKK-WLAN-ACCESS", "atkkWiAcClientChannel"),
        ("ATKK-WLAN-ACCESS", "atkkWiAcClientAge"),
        ("ATKK-WLAN-ACCESS", "atkkWiAcClientUserID"))
)
if mibBuilder.loadTexts:
    atkkWiAcAssociated.setStatus(
        "current"
    )

atkkWiAcDisassociated = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 5, 0, 2)
)
atkkWiAcDisassociated.setObjects(
      *(("ATKK-WLAN-ACCESS", "atkkWiAcClientAddress"),
        ("ATKK-WLAN-ACCESS", "atkkWiAcClientSSID"),
        ("ATKK-WLAN-ACCESS", "atkkWiAcClient80211Spec"),
        ("ATKK-WLAN-ACCESS", "atkkWiAcClientChannel"),
        ("ATKK-WLAN-ACCESS", "atkkWiAcClientAge"),
        ("ATKK-WLAN-ACCESS", "atkkWiAcClientUserID"))
)
if mibBuilder.loadTexts:
    atkkWiAcDisassociated.setStatus(
        "current"
    )

atkkWiAcUnknownAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 5, 0, 3)
)
atkkWiAcUnknownAP.setObjects(
      *(("ATKK-WLAN-ACCESS", "atkkWiAcAPAddress"),
        ("ATKK-WLAN-ACCESS", "atkkWiAcAPSSID"),
        ("ATKK-WLAN-ACCESS", "atkkWiAcAP80211Spec"),
        ("ATKK-WLAN-ACCESS", "atkkWiAcAPChannel"),
        ("ATKK-WLAN-ACCESS", "atkkWiAcAPRSSI"))
)
if mibBuilder.loadTexts:
    atkkWiAcUnknownAP.setStatus(
        "current"
    )

atkkWiAcFiltered = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 5, 0, 4)
)
atkkWiAcFiltered.setObjects(
      *(("ATKK-WLAN-ACCESS", "atkkWiAcClientAddress"),
        ("ATKK-WLAN-ACCESS", "atkkWiAcClientSSID"),
        ("ATKK-WLAN-ACCESS", "atkkWiAcClient80211Spec"),
        ("ATKK-WLAN-ACCESS", "atkkWiAcClientChannel"),
        ("ATKK-WLAN-ACCESS", "atkkWiAcClientAge"),
        ("ATKK-WLAN-ACCESS", "atkkWiAcClientUserID"))
)
if mibBuilder.loadTexts:
    atkkWiAcFiltered.setStatus(
        "current"
    )

atkkWiAcRadiusAuthSucceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 5, 0, 5)
)
atkkWiAcRadiusAuthSucceeded.setObjects(
      *(("ATKK-WLAN-ACCESS", "atkkWiAcClientAddress"),
        ("ATKK-WLAN-ACCESS", "atkkWiAcClientSSID"),
        ("ATKK-WLAN-ACCESS", "atkkWiAcClientUserID"))
)
if mibBuilder.loadTexts:
    atkkWiAcRadiusAuthSucceeded.setStatus(
        "current"
    )

atkkWiAcRadiusAuthFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 5, 0, 6)
)
atkkWiAcRadiusAuthFailed.setObjects(
      *(("ATKK-WLAN-ACCESS", "atkkWiAcClientAddress"),
        ("ATKK-WLAN-ACCESS", "atkkWiAcClientSSID"),
        ("ATKK-WLAN-ACCESS", "atkkWiAcClientUserID"))
)
if mibBuilder.loadTexts:
    atkkWiAcRadiusAuthFailed.setStatus(
        "current"
    )

atkkWiAcRadarDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 5, 0, 7)
)
atkkWiAcRadarDetected.setObjects(
      *(("ATKK-WLAN-ACCESS", "atkkWiAcAPRadarDetected"),
        ("ATKK-WLAN-ACCESS", "atkkWiAcAPChannels"))
)
if mibBuilder.loadTexts:
    atkkWiAcRadarDetected.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ATKK-WLAN-ACCESS",
    **{"SsidString": SsidString,
       "UserIdString": UserIdString,
       "TrapHostString": TrapHostString,
       "CommunityString": CommunityString,
       "TrapString": TrapString,
       "ChannelString": ChannelString,
       "tq2403": tq2403,
       "tq2450": tq2450,
       "tq2403ex": tq2403ex,
       "tq3600": tq3600,
       "tq3200": tq3200,
       "tq3400": tq3400,
       "tq4400": tq4400,
       "tq4600": tq4600,
       "tq4400e": tq4400e,
       "atkkWlanAccess": atkkWlanAccess,
       "atkkWiAcVersion": atkkWiAcVersion,
       "atkkWiAcClients": atkkWiAcClients,
       "atkkWiAcClientTable": atkkWiAcClientTable,
       "atkkWiAcClientEntry": atkkWiAcClientEntry,
       "atkkWiAcClientAddress": atkkWiAcClientAddress,
       "atkkWiAcClientSSID": atkkWiAcClientSSID,
       "atkkWiAcClient80211Spec": atkkWiAcClient80211Spec,
       "atkkWiAcClientChannel": atkkWiAcClientChannel,
       "atkkWiAcClientAge": atkkWiAcClientAge,
       "atkkWiAcClientUserID": atkkWiAcClientUserID,
       "atkkWiAcAPs": atkkWiAcAPs,
       "atkkWiAcAPTable": atkkWiAcAPTable,
       "atkkWiAcAPEntry": atkkWiAcAPEntry,
       "atkkWiAcAPAddress": atkkWiAcAPAddress,
       "atkkWiAcAPSSID": atkkWiAcAPSSID,
       "atkkWiAcAP80211Spec": atkkWiAcAP80211Spec,
       "atkkWiAcAPChannel": atkkWiAcAPChannel,
       "atkkWiAcAPRSSI": atkkWiAcAPRSSI,
       "atkkWiAcAPRadarDetected": atkkWiAcAPRadarDetected,
       "atkkWiAcAPChannels": atkkWiAcAPChannels,
       "atkkWiAcAPDetectConfig": atkkWiAcAPDetectConfig,
       "atkkWiAcAPDetectConfig2": atkkWiAcAPDetectConfig2,
       "atkkWiAcMacACL": atkkWiAcMacACL,
       "atkkWiAcMacACLTable": atkkWiAcMacACLTable,
       "atkkWiAcMacACLEntry": atkkWiAcMacACLEntry,
       "atkkWiAcMacACLAddress": atkkWiAcMacACLAddress,
       "atkkWiAcMacACLModeConfig": atkkWiAcMacACLModeConfig,
       "atkkWiAcNotification": atkkWiAcNotification,
       "atkkWiAcNotificationObjects": atkkWiAcNotificationObjects,
       "atkkWiAcAssociated": atkkWiAcAssociated,
       "atkkWiAcDisassociated": atkkWiAcDisassociated,
       "atkkWiAcUnknownAP": atkkWiAcUnknownAP,
       "atkkWiAcFiltered": atkkWiAcFiltered,
       "atkkWiAcRadiusAuthSucceeded": atkkWiAcRadiusAuthSucceeded,
       "atkkWiAcRadiusAuthFailed": atkkWiAcRadiusAuthFailed,
       "atkkWiAcRadarDetected": atkkWiAcRadarDetected,
       "atkkWiAcApInfo": atkkWiAcApInfo,
       "atkkWiAcApInfoTrapTable": atkkWiAcApInfoTrapTable,
       "atkkWiAcApInfoTrapEntry": atkkWiAcApInfoTrapEntry,
       "atkkWiAcApTrapHost": atkkWiAcApTrapHost,
       "atkkWiAcApTrapCommunity": atkkWiAcApTrapCommunity,
       "atkkWiAcApTrapColdStartConfig": atkkWiAcApTrapColdStartConfig,
       "atkkWiAcApTrapLinkConfig": atkkWiAcApTrapLinkConfig,
       "atkkWiAcApTrapAuthenticationConfig": atkkWiAcApTrapAuthenticationConfig,
       "atkkWiAcApTrapAssociationConfig": atkkWiAcApTrapAssociationConfig,
       "atkkWiAcApTrapUnknownApConfig": atkkWiAcApTrapUnknownApConfig,
       "atkkWiAcApTrapFilteredStaConfig": atkkWiAcApTrapFilteredStaConfig,
       "atkkWiAcApTrapRadiusAuthSuccessConfig": atkkWiAcApTrapRadiusAuthSuccessConfig,
       "atkkWiAcApTrapRadiusAuthFailConfig": atkkWiAcApTrapRadiusAuthFailConfig,
       "atkkWiAcApTrapDfsDetectedConfig": atkkWiAcApTrapDfsDetectedConfig}
)
