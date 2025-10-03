# SNMP MIB module (RUCKUS-ZD-WLAN-CONFIG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ruckus\RUCKUS-ZD-WLAN-CONFIG-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:24:08 2025
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

(ruckusZDWLANModule,) = mibBuilder.importSymbols(
    "RUCKUS-ROOT-MIB",
    "ruckusZDWLANModule")

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

ruckusZDWLANConfigMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuckusZDWLANConfigObjects_ObjectIdentity = ObjectIdentity
ruckusZDWLANConfigObjects = _RuckusZDWLANConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1)
)
_RuckusZDWLANConfig_ObjectIdentity = ObjectIdentity
ruckusZDWLANConfig = _RuckusZDWLANConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1)
)
_RuckusZDWLANConfigTable_Object = MibTable
ruckusZDWLANConfigTable = _RuckusZDWLANConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ruckusZDWLANConfigTable.setStatus("current")
_RuckusZDWLANConfigEntry_Object = MibTableRow
ruckusZDWLANConfigEntry = _RuckusZDWLANConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 1, 1)
)
ruckusZDWLANConfigEntry.setIndexNames(
    (0, "RUCKUS-ZD-WLAN-CONFIG-MIB", "ruckusZDWLANID"),
)
if mibBuilder.loadTexts:
    ruckusZDWLANConfigEntry.setStatus("current")


class _RuckusZDWLANID_Type(Integer32):
    """Custom type ruckusZDWLANID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2048),
    )


_RuckusZDWLANID_Type.__name__ = "Integer32"
_RuckusZDWLANID_Object = MibTableColumn
ruckusZDWLANID = _RuckusZDWLANID_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 1, 1, 1),
    _RuckusZDWLANID_Type()
)
ruckusZDWLANID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruckusZDWLANID.setStatus("current")


class _RuckusZDWLANConfigSSID_Type(OctetString):
    """Custom type ruckusZDWLANConfigSSID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 32),
    )


_RuckusZDWLANConfigSSID_Type.__name__ = "OctetString"
_RuckusZDWLANConfigSSID_Object = MibTableColumn
ruckusZDWLANConfigSSID = _RuckusZDWLANConfigSSID_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 1, 1, 2),
    _RuckusZDWLANConfigSSID_Type()
)
ruckusZDWLANConfigSSID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDWLANConfigSSID.setStatus("current")


class _RuckusZDWLANConfigDescription_Type(DisplayString):
    """Custom type ruckusZDWLANConfigDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_RuckusZDWLANConfigDescription_Type.__name__ = "DisplayString"
_RuckusZDWLANConfigDescription_Object = MibTableColumn
ruckusZDWLANConfigDescription = _RuckusZDWLANConfigDescription_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 1, 1, 3),
    _RuckusZDWLANConfigDescription_Type()
)
ruckusZDWLANConfigDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDWLANConfigDescription.setStatus("current")


class _RuckusZDWLANConfigName_Type(OctetString):
    """Custom type ruckusZDWLANConfigName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 32),
    )


_RuckusZDWLANConfigName_Type.__name__ = "OctetString"
_RuckusZDWLANConfigName_Object = MibTableColumn
ruckusZDWLANConfigName = _RuckusZDWLANConfigName_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 1, 1, 4),
    _RuckusZDWLANConfigName_Type()
)
ruckusZDWLANConfigName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDWLANConfigName.setStatus("current")


class _RuckusZDWLANConfigWLANServiceType_Type(Integer32):
    """Custom type ruckusZDWLANConfigWLANServiceType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("standardUsage", 1),
          ("guestAccess", 2),
          ("hotSpotService", 3))
    )


_RuckusZDWLANConfigWLANServiceType_Type.__name__ = "Integer32"
_RuckusZDWLANConfigWLANServiceType_Object = MibTableColumn
ruckusZDWLANConfigWLANServiceType = _RuckusZDWLANConfigWLANServiceType_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 1, 1, 8),
    _RuckusZDWLANConfigWLANServiceType_Type()
)
ruckusZDWLANConfigWLANServiceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDWLANConfigWLANServiceType.setStatus("current")


class _RuckusZDWLANConfigAuthentication_Type(Integer32):
    """Custom type ruckusZDWLANConfigAuthentication based on Integer32"""
    defaultValue = 1

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
        *(("open", 1),
          ("shared", 2),
          ("eap", 3),
          ("mac-address", 4),
          ("eap-mac-mix", 5))
    )


_RuckusZDWLANConfigAuthentication_Type.__name__ = "Integer32"
_RuckusZDWLANConfigAuthentication_Object = MibTableColumn
ruckusZDWLANConfigAuthentication = _RuckusZDWLANConfigAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 1, 1, 10),
    _RuckusZDWLANConfigAuthentication_Type()
)
ruckusZDWLANConfigAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDWLANConfigAuthentication.setStatus("current")


class _RuckusZDWLANConfigEncryption_Type(Integer32):
    """Custom type ruckusZDWLANConfigEncryption based on Integer32"""
    defaultValue = 6

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
        *(("wpa", 1),
          ("wpa2", 2),
          ("wpa-Mixed", 3),
          ("wep-64", 4),
          ("wep-128", 5),
          ("none-enc", 6))
    )


_RuckusZDWLANConfigEncryption_Type.__name__ = "Integer32"
_RuckusZDWLANConfigEncryption_Object = MibTableColumn
ruckusZDWLANConfigEncryption = _RuckusZDWLANConfigEncryption_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 1, 1, 12),
    _RuckusZDWLANConfigEncryption_Type()
)
ruckusZDWLANConfigEncryption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDWLANConfigEncryption.setStatus("current")


class _RuckusZDWLANConfigWEPKeyIndex_Type(Integer32):
    """Custom type ruckusZDWLANConfigWEPKeyIndex based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_RuckusZDWLANConfigWEPKeyIndex_Type.__name__ = "Integer32"
_RuckusZDWLANConfigWEPKeyIndex_Object = MibTableColumn
ruckusZDWLANConfigWEPKeyIndex = _RuckusZDWLANConfigWEPKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 1, 1, 15),
    _RuckusZDWLANConfigWEPKeyIndex_Type()
)
ruckusZDWLANConfigWEPKeyIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDWLANConfigWEPKeyIndex.setStatus("current")


class _RuckusZDWLANConfigWEPKey_Type(OctetString):
    """Custom type ruckusZDWLANConfigWEPKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
        ValueSizeConstraint(26, 26),
    )


_RuckusZDWLANConfigWEPKey_Type.__name__ = "OctetString"
_RuckusZDWLANConfigWEPKey_Object = MibTableColumn
ruckusZDWLANConfigWEPKey = _RuckusZDWLANConfigWEPKey_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 1, 1, 16),
    _RuckusZDWLANConfigWEPKey_Type()
)
ruckusZDWLANConfigWEPKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDWLANConfigWEPKey.setStatus("current")


class _RuckusZDWLANConfigWPACipherType_Type(Integer32):
    """Custom type ruckusZDWLANConfigWPACipherType based on Integer32"""
    defaultValue = 0

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
          ("tkip", 1),
          ("aes", 2),
          ("auto", 3))
    )


_RuckusZDWLANConfigWPACipherType_Type.__name__ = "Integer32"
_RuckusZDWLANConfigWPACipherType_Object = MibTableColumn
ruckusZDWLANConfigWPACipherType = _RuckusZDWLANConfigWPACipherType_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 1, 1, 20),
    _RuckusZDWLANConfigWPACipherType_Type()
)
ruckusZDWLANConfigWPACipherType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDWLANConfigWPACipherType.setStatus("current")


class _RuckusZDWLANConfigWPAKey_Type(OctetString):
    """Custom type ruckusZDWLANConfigWPAKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 63),
        ValueSizeConstraint(64, 64),
    )


_RuckusZDWLANConfigWPAKey_Type.__name__ = "OctetString"
_RuckusZDWLANConfigWPAKey_Object = MibTableColumn
ruckusZDWLANConfigWPAKey = _RuckusZDWLANConfigWPAKey_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 1, 1, 21),
    _RuckusZDWLANConfigWPAKey_Type()
)
ruckusZDWLANConfigWPAKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDWLANConfigWPAKey.setStatus("current")
_RuckusZDWLANConfigAuthenticationServerID_Type = Integer32
_RuckusZDWLANConfigAuthenticationServerID_Object = MibTableColumn
ruckusZDWLANConfigAuthenticationServerID = _RuckusZDWLANConfigAuthenticationServerID_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 1, 1, 25),
    _RuckusZDWLANConfigAuthenticationServerID_Type()
)
ruckusZDWLANConfigAuthenticationServerID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDWLANConfigAuthenticationServerID.setStatus("current")


class _RuckusZDWLANConfigWirelessClientIsolation_Type(Integer32):
    """Custom type ruckusZDWLANConfigWirelessClientIsolation based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RuckusZDWLANConfigWirelessClientIsolation_Type.__name__ = "Integer32"
_RuckusZDWLANConfigWirelessClientIsolation_Object = MibTableColumn
ruckusZDWLANConfigWirelessClientIsolation = _RuckusZDWLANConfigWirelessClientIsolation_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 1, 1, 28),
    _RuckusZDWLANConfigWirelessClientIsolation_Type()
)
ruckusZDWLANConfigWirelessClientIsolation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDWLANConfigWirelessClientIsolation.setStatus("current")


class _RuckusZDWLANConfigWirelessWhiteListID_Type(Integer32):
    """Custom type ruckusZDWLANConfigWirelessWhiteListID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_RuckusZDWLANConfigWirelessWhiteListID_Type.__name__ = "Integer32"
_RuckusZDWLANConfigWirelessWhiteListID_Object = MibTableColumn
ruckusZDWLANConfigWirelessWhiteListID = _RuckusZDWLANConfigWirelessWhiteListID_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 1, 1, 29),
    _RuckusZDWLANConfigWirelessWhiteListID_Type()
)
ruckusZDWLANConfigWirelessWhiteListID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDWLANConfigWirelessWhiteListID.setStatus("current")


class _RuckusZDWLANConfigZeroITActivation_Type(Integer32):
    """Custom type ruckusZDWLANConfigZeroITActivation based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RuckusZDWLANConfigZeroITActivation_Type.__name__ = "Integer32"
_RuckusZDWLANConfigZeroITActivation_Object = MibTableColumn
ruckusZDWLANConfigZeroITActivation = _RuckusZDWLANConfigZeroITActivation_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 1, 1, 30),
    _RuckusZDWLANConfigZeroITActivation_Type()
)
ruckusZDWLANConfigZeroITActivation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDWLANConfigZeroITActivation.setStatus("current")


class _RuckusZDWLANConfigWLANHotspotID_Type(Integer32):
    """Custom type ruckusZDWLANConfigWLANHotspotID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_RuckusZDWLANConfigWLANHotspotID_Type.__name__ = "Integer32"
_RuckusZDWLANConfigWLANHotspotID_Object = MibTableColumn
ruckusZDWLANConfigWLANHotspotID = _RuckusZDWLANConfigWLANHotspotID_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 1, 1, 31),
    _RuckusZDWLANConfigWLANHotspotID_Type()
)
ruckusZDWLANConfigWLANHotspotID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDWLANConfigWLANHotspotID.setStatus("current")


class _RuckusZDWLANConfigWLANServicePriority_Type(Integer32):
    """Custom type ruckusZDWLANConfigWLANServicePriority based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("low", 2))
    )


_RuckusZDWLANConfigWLANServicePriority_Type.__name__ = "Integer32"
_RuckusZDWLANConfigWLANServicePriority_Object = MibTableColumn
ruckusZDWLANConfigWLANServicePriority = _RuckusZDWLANConfigWLANServicePriority_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 1, 1, 32),
    _RuckusZDWLANConfigWLANServicePriority_Type()
)
ruckusZDWLANConfigWLANServicePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDWLANConfigWLANServicePriority.setStatus("current")


class _RuckusZDWLANConfigAccountingServerID_Type(Integer32):
    """Custom type ruckusZDWLANConfigAccountingServerID based on Integer32"""
    defaultValue = 0


_RuckusZDWLANConfigAccountingServerID_Type.__name__ = "Integer32"
_RuckusZDWLANConfigAccountingServerID_Object = MibTableColumn
ruckusZDWLANConfigAccountingServerID = _RuckusZDWLANConfigAccountingServerID_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 1, 1, 35),
    _RuckusZDWLANConfigAccountingServerID_Type()
)
ruckusZDWLANConfigAccountingServerID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDWLANConfigAccountingServerID.setStatus("current")


class _RuckusZDWLANConfigAccountingUpdateInterval_Type(Integer32):
    """Custom type ruckusZDWLANConfigAccountingUpdateInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_RuckusZDWLANConfigAccountingUpdateInterval_Type.__name__ = "Integer32"
_RuckusZDWLANConfigAccountingUpdateInterval_Object = MibTableColumn
ruckusZDWLANConfigAccountingUpdateInterval = _RuckusZDWLANConfigAccountingUpdateInterval_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 1, 1, 36),
    _RuckusZDWLANConfigAccountingUpdateInterval_Type()
)
ruckusZDWLANConfigAccountingUpdateInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDWLANConfigAccountingUpdateInterval.setStatus("current")


class _RuckusZDWLANConfigUplinkRate_Type(OctetString):
    """Custom type ruckusZDWLANConfigUplinkRate based on OctetString"""
    defaultValue = OctetString("disable")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_RuckusZDWLANConfigUplinkRate_Type.__name__ = "OctetString"
_RuckusZDWLANConfigUplinkRate_Object = MibTableColumn
ruckusZDWLANConfigUplinkRate = _RuckusZDWLANConfigUplinkRate_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 1, 1, 40),
    _RuckusZDWLANConfigUplinkRate_Type()
)
ruckusZDWLANConfigUplinkRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDWLANConfigUplinkRate.setStatus("current")


class _RuckusZDWLANConfigDownlinkRate_Type(OctetString):
    """Custom type ruckusZDWLANConfigDownlinkRate based on OctetString"""
    defaultValue = OctetString("disable")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_RuckusZDWLANConfigDownlinkRate_Type.__name__ = "OctetString"
_RuckusZDWLANConfigDownlinkRate_Object = MibTableColumn
ruckusZDWLANConfigDownlinkRate = _RuckusZDWLANConfigDownlinkRate_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 1, 1, 41),
    _RuckusZDWLANConfigDownlinkRate_Type()
)
ruckusZDWLANConfigDownlinkRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDWLANConfigDownlinkRate.setStatus("current")


class _RuckusZDWLANConfigIGMPSnooping_Type(Integer32):
    """Custom type ruckusZDWLANConfigIGMPSnooping based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RuckusZDWLANConfigIGMPSnooping_Type.__name__ = "Integer32"
_RuckusZDWLANConfigIGMPSnooping_Object = MibTableColumn
ruckusZDWLANConfigIGMPSnooping = _RuckusZDWLANConfigIGMPSnooping_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 1, 1, 42),
    _RuckusZDWLANConfigIGMPSnooping_Type()
)
ruckusZDWLANConfigIGMPSnooping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDWLANConfigIGMPSnooping.setStatus("current")


class _RuckusZDWLANConfigVlanID_Type(Integer32):
    """Custom type ruckusZDWLANConfigVlanID based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_RuckusZDWLANConfigVlanID_Type.__name__ = "Integer32"
_RuckusZDWLANConfigVlanID_Object = MibTableColumn
ruckusZDWLANConfigVlanID = _RuckusZDWLANConfigVlanID_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 1, 1, 45),
    _RuckusZDWLANConfigVlanID_Type()
)
ruckusZDWLANConfigVlanID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDWLANConfigVlanID.setStatus("current")


class _RuckusZDWLANConfigDynamicVLAN_Type(Integer32):
    """Custom type ruckusZDWLANConfigDynamicVLAN based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RuckusZDWLANConfigDynamicVLAN_Type.__name__ = "Integer32"
_RuckusZDWLANConfigDynamicVLAN_Object = MibTableColumn
ruckusZDWLANConfigDynamicVLAN = _RuckusZDWLANConfigDynamicVLAN_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 1, 1, 46),
    _RuckusZDWLANConfigDynamicVLAN_Type()
)
ruckusZDWLANConfigDynamicVLAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDWLANConfigDynamicVLAN.setStatus("current")


class _RuckusZDWLANConfigHideSSID_Type(TruthValue):
    """Custom type ruckusZDWLANConfigHideSSID based on TruthValue"""
    defaultValue = 2


_RuckusZDWLANConfigHideSSID_Type.__name__ = "TruthValue"
_RuckusZDWLANConfigHideSSID_Object = MibTableColumn
ruckusZDWLANConfigHideSSID = _RuckusZDWLANConfigHideSSID_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 1, 1, 50),
    _RuckusZDWLANConfigHideSSID_Type()
)
ruckusZDWLANConfigHideSSID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDWLANConfigHideSSID.setStatus("current")


class _RuckusZDWLANConfigTunnelMode_Type(TruthValue):
    """Custom type ruckusZDWLANConfigTunnelMode based on TruthValue"""
    defaultValue = 2


_RuckusZDWLANConfigTunnelMode_Type.__name__ = "TruthValue"
_RuckusZDWLANConfigTunnelMode_Object = MibTableColumn
ruckusZDWLANConfigTunnelMode = _RuckusZDWLANConfigTunnelMode_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 1, 1, 52),
    _RuckusZDWLANConfigTunnelMode_Type()
)
ruckusZDWLANConfigTunnelMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDWLANConfigTunnelMode.setStatus("current")


class _RuckusZDWLANConfigBackgroundScanning_Type(TruthValue):
    """Custom type ruckusZDWLANConfigBackgroundScanning based on TruthValue"""
    defaultValue = 2


_RuckusZDWLANConfigBackgroundScanning_Type.__name__ = "TruthValue"
_RuckusZDWLANConfigBackgroundScanning_Object = MibTableColumn
ruckusZDWLANConfigBackgroundScanning = _RuckusZDWLANConfigBackgroundScanning_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 1, 1, 53),
    _RuckusZDWLANConfigBackgroundScanning_Type()
)
ruckusZDWLANConfigBackgroundScanning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDWLANConfigBackgroundScanning.setStatus("current")


class _RuckusZDWLANConfigMaxClients_Type(Integer32):
    """Custom type ruckusZDWLANConfigMaxClients based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_RuckusZDWLANConfigMaxClients_Type.__name__ = "Integer32"
_RuckusZDWLANConfigMaxClients_Object = MibTableColumn
ruckusZDWLANConfigMaxClients = _RuckusZDWLANConfigMaxClients_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 1, 1, 55),
    _RuckusZDWLANConfigMaxClients_Type()
)
ruckusZDWLANConfigMaxClients.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDWLANConfigMaxClients.setStatus("current")


class _RuckusZDWLANConfigWebAuthentication_Type(Integer32):
    """Custom type ruckusZDWLANConfigWebAuthentication based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RuckusZDWLANConfigWebAuthentication_Type.__name__ = "Integer32"
_RuckusZDWLANConfigWebAuthentication_Object = MibTableColumn
ruckusZDWLANConfigWebAuthentication = _RuckusZDWLANConfigWebAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 1, 1, 60),
    _RuckusZDWLANConfigWebAuthentication_Type()
)
ruckusZDWLANConfigWebAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDWLANConfigWebAuthentication.setStatus("current")
_RuckusZDWLANConfigRowStatus_Type = RowStatus
_RuckusZDWLANConfigRowStatus_Object = MibTableColumn
ruckusZDWLANConfigRowStatus = _RuckusZDWLANConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 1, 1, 63),
    _RuckusZDWLANConfigRowStatus_Type()
)
ruckusZDWLANConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruckusZDWLANConfigRowStatus.setStatus("current")
_RuckusZDWLANGroupConfigTable_Object = MibTable
ruckusZDWLANGroupConfigTable = _RuckusZDWLANGroupConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 2)
)
if mibBuilder.loadTexts:
    ruckusZDWLANGroupConfigTable.setStatus("current")
_RuckusZDWLANGroupConfigEntry_Object = MibTableRow
ruckusZDWLANGroupConfigEntry = _RuckusZDWLANGroupConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 2, 1)
)
ruckusZDWLANGroupConfigEntry.setIndexNames(
    (0, "RUCKUS-ZD-WLAN-CONFIG-MIB", "ruckusZDWLANGroupID"),
)
if mibBuilder.loadTexts:
    ruckusZDWLANGroupConfigEntry.setStatus("current")


class _RuckusZDWLANGroupID_Type(Integer32):
    """Custom type ruckusZDWLANGroupID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2048),
    )


_RuckusZDWLANGroupID_Type.__name__ = "Integer32"
_RuckusZDWLANGroupID_Object = MibTableColumn
ruckusZDWLANGroupID = _RuckusZDWLANGroupID_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 2, 1, 1),
    _RuckusZDWLANGroupID_Type()
)
ruckusZDWLANGroupID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruckusZDWLANGroupID.setStatus("current")


class _RuckusZDWLANGroupConfigName_Type(DisplayString):
    """Custom type ruckusZDWLANGroupConfigName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RuckusZDWLANGroupConfigName_Type.__name__ = "DisplayString"
_RuckusZDWLANGroupConfigName_Object = MibTableColumn
ruckusZDWLANGroupConfigName = _RuckusZDWLANGroupConfigName_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 2, 1, 5),
    _RuckusZDWLANGroupConfigName_Type()
)
ruckusZDWLANGroupConfigName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDWLANGroupConfigName.setStatus("current")


class _RuckusZDWLANGroupConfigDescription_Type(DisplayString):
    """Custom type ruckusZDWLANGroupConfigDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_RuckusZDWLANGroupConfigDescription_Type.__name__ = "DisplayString"
_RuckusZDWLANGroupConfigDescription_Object = MibTableColumn
ruckusZDWLANGroupConfigDescription = _RuckusZDWLANGroupConfigDescription_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 2, 1, 6),
    _RuckusZDWLANGroupConfigDescription_Type()
)
ruckusZDWLANGroupConfigDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDWLANGroupConfigDescription.setStatus("current")
_RuckusZDWLANGroupVlanOverrideStatus_Type = TruthValue
_RuckusZDWLANGroupVlanOverrideStatus_Object = MibTableColumn
ruckusZDWLANGroupVlanOverrideStatus = _RuckusZDWLANGroupVlanOverrideStatus_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 2, 1, 8),
    _RuckusZDWLANGroupVlanOverrideStatus_Type()
)
ruckusZDWLANGroupVlanOverrideStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANGroupVlanOverrideStatus.setStatus("current")
_RuckusZDWLANGroupConfigRowStatus_Type = RowStatus
_RuckusZDWLANGroupConfigRowStatus_Object = MibTableColumn
ruckusZDWLANGroupConfigRowStatus = _RuckusZDWLANGroupConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 2, 1, 15),
    _RuckusZDWLANGroupConfigRowStatus_Type()
)
ruckusZDWLANGroupConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruckusZDWLANGroupConfigRowStatus.setStatus("current")
_RuckusZDWLANGroupCfgAttrTable_Object = MibTable
ruckusZDWLANGroupCfgAttrTable = _RuckusZDWLANGroupCfgAttrTable_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 3)
)
if mibBuilder.loadTexts:
    ruckusZDWLANGroupCfgAttrTable.setStatus("current")
_RuckusZDWLANGroupCfgAttrEntry_Object = MibTableRow
ruckusZDWLANGroupCfgAttrEntry = _RuckusZDWLANGroupCfgAttrEntry_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 3, 1)
)
ruckusZDWLANGroupCfgAttrEntry.setIndexNames(
    (0, "RUCKUS-ZD-WLAN-CONFIG-MIB", "ruckusZDWLANGroupID"),
    (0, "RUCKUS-ZD-WLAN-CONFIG-MIB", "ruckusZDWLANID"),
)
if mibBuilder.loadTexts:
    ruckusZDWLANGroupCfgAttrEntry.setStatus("current")


class _RuckusZDWLANGroupCfgAttrOverrideType_Type(Integer32):
    """Custom type ruckusZDWLANGroupCfgAttrOverrideType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nochange", 1),
          ("tag", 2))
    )


_RuckusZDWLANGroupCfgAttrOverrideType_Type.__name__ = "Integer32"
_RuckusZDWLANGroupCfgAttrOverrideType_Object = MibTableColumn
ruckusZDWLANGroupCfgAttrOverrideType = _RuckusZDWLANGroupCfgAttrOverrideType_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 3, 1, 3),
    _RuckusZDWLANGroupCfgAttrOverrideType_Type()
)
ruckusZDWLANGroupCfgAttrOverrideType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDWLANGroupCfgAttrOverrideType.setStatus("current")


class _RuckusZDWLANGroupCfgAttrWGVlanTag_Type(Integer32):
    """Custom type ruckusZDWLANGroupCfgAttrWGVlanTag based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_RuckusZDWLANGroupCfgAttrWGVlanTag_Type.__name__ = "Integer32"
_RuckusZDWLANGroupCfgAttrWGVlanTag_Object = MibTableColumn
ruckusZDWLANGroupCfgAttrWGVlanTag = _RuckusZDWLANGroupCfgAttrWGVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 3, 1, 4),
    _RuckusZDWLANGroupCfgAttrWGVlanTag_Type()
)
ruckusZDWLANGroupCfgAttrWGVlanTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDWLANGroupCfgAttrWGVlanTag.setStatus("current")
_RuckusZDWLANGroupCfgAttrRowStatus_Type = RowStatus
_RuckusZDWLANGroupCfgAttrRowStatus_Object = MibTableColumn
ruckusZDWLANGroupCfgAttrRowStatus = _RuckusZDWLANGroupCfgAttrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 3, 1, 10),
    _RuckusZDWLANGroupCfgAttrRowStatus_Type()
)
ruckusZDWLANGroupCfgAttrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruckusZDWLANGroupCfgAttrRowStatus.setStatus("current")
_RuckusZDHotspotConfigTable_Object = MibTable
ruckusZDHotspotConfigTable = _RuckusZDHotspotConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 8)
)
if mibBuilder.loadTexts:
    ruckusZDHotspotConfigTable.setStatus("current")
_RuckusZDHotspotConfigEntry_Object = MibTableRow
ruckusZDHotspotConfigEntry = _RuckusZDHotspotConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 8, 1)
)
ruckusZDHotspotConfigEntry.setIndexNames(
    (0, "RUCKUS-ZD-WLAN-CONFIG-MIB", "ruckusZDHotspotID"),
)
if mibBuilder.loadTexts:
    ruckusZDHotspotConfigEntry.setStatus("current")


class _RuckusZDHotspotID_Type(Integer32):
    """Custom type ruckusZDHotspotID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_RuckusZDHotspotID_Type.__name__ = "Integer32"
_RuckusZDHotspotID_Object = MibTableColumn
ruckusZDHotspotID = _RuckusZDHotspotID_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 8, 1, 1),
    _RuckusZDHotspotID_Type()
)
ruckusZDHotspotID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruckusZDHotspotID.setStatus("current")


class _RuckusZDHotspotName_Type(DisplayString):
    """Custom type ruckusZDHotspotName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RuckusZDHotspotName_Type.__name__ = "DisplayString"
_RuckusZDHotspotName_Object = MibTableColumn
ruckusZDHotspotName = _RuckusZDHotspotName_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 8, 1, 2),
    _RuckusZDHotspotName_Type()
)
ruckusZDHotspotName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDHotspotName.setStatus("current")


class _RuckusZDHotspotRedirectLoginPage_Type(DisplayString):
    """Custom type ruckusZDHotspotRedirectLoginPage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_RuckusZDHotspotRedirectLoginPage_Type.__name__ = "DisplayString"
_RuckusZDHotspotRedirectLoginPage_Object = MibTableColumn
ruckusZDHotspotRedirectLoginPage = _RuckusZDHotspotRedirectLoginPage_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 8, 1, 3),
    _RuckusZDHotspotRedirectLoginPage_Type()
)
ruckusZDHotspotRedirectLoginPage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDHotspotRedirectLoginPage.setStatus("current")


class _RuckusZDHotspotRedirectStartURL_Type(DisplayString):
    """Custom type ruckusZDHotspotRedirectStartURL based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_RuckusZDHotspotRedirectStartURL_Type.__name__ = "DisplayString"
_RuckusZDHotspotRedirectStartURL_Object = MibTableColumn
ruckusZDHotspotRedirectStartURL = _RuckusZDHotspotRedirectStartURL_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 8, 1, 4),
    _RuckusZDHotspotRedirectStartURL_Type()
)
ruckusZDHotspotRedirectStartURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDHotspotRedirectStartURL.setStatus("current")


class _RuckusZDHotspotRedirectType_Type(Integer32):
    """Custom type ruckusZDHotspotRedirectType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("user", 1),
          ("url", 2))
    )


_RuckusZDHotspotRedirectType_Type.__name__ = "Integer32"
_RuckusZDHotspotRedirectType_Object = MibTableColumn
ruckusZDHotspotRedirectType = _RuckusZDHotspotRedirectType_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 8, 1, 6),
    _RuckusZDHotspotRedirectType_Type()
)
ruckusZDHotspotRedirectType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDHotspotRedirectType.setStatus("current")
_RuckusZDHotspotRowStatus_Type = RowStatus
_RuckusZDHotspotRowStatus_Object = MibTableColumn
ruckusZDHotspotRowStatus = _RuckusZDHotspotRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 8, 1, 15),
    _RuckusZDHotspotRowStatus_Type()
)
ruckusZDHotspotRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruckusZDHotspotRowStatus.setStatus("current")
_RuckusZDClientIsolationWhiteListTable_Object = MibTable
ruckusZDClientIsolationWhiteListTable = _RuckusZDClientIsolationWhiteListTable_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 15)
)
if mibBuilder.loadTexts:
    ruckusZDClientIsolationWhiteListTable.setStatus("current")
_RuckusZDClientIsolationWhiteListEntry_Object = MibTableRow
ruckusZDClientIsolationWhiteListEntry = _RuckusZDClientIsolationWhiteListEntry_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 15, 1)
)
ruckusZDClientIsolationWhiteListEntry.setIndexNames(
    (0, "RUCKUS-ZD-WLAN-CONFIG-MIB", "ruckusZDClientIsolationWhiteListID"),
)
if mibBuilder.loadTexts:
    ruckusZDClientIsolationWhiteListEntry.setStatus("current")


class _RuckusZDClientIsolationWhiteListID_Type(Integer32):
    """Custom type ruckusZDClientIsolationWhiteListID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_RuckusZDClientIsolationWhiteListID_Type.__name__ = "Integer32"
_RuckusZDClientIsolationWhiteListID_Object = MibTableColumn
ruckusZDClientIsolationWhiteListID = _RuckusZDClientIsolationWhiteListID_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 15, 1, 1),
    _RuckusZDClientIsolationWhiteListID_Type()
)
ruckusZDClientIsolationWhiteListID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruckusZDClientIsolationWhiteListID.setStatus("current")


class _RuckusZDClientIsolationWhiteListName_Type(DisplayString):
    """Custom type ruckusZDClientIsolationWhiteListName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RuckusZDClientIsolationWhiteListName_Type.__name__ = "DisplayString"
_RuckusZDClientIsolationWhiteListName_Object = MibTableColumn
ruckusZDClientIsolationWhiteListName = _RuckusZDClientIsolationWhiteListName_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 15, 1, 5),
    _RuckusZDClientIsolationWhiteListName_Type()
)
ruckusZDClientIsolationWhiteListName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDClientIsolationWhiteListName.setStatus("current")


class _RuckusZDClientIsolationWhiteListDescription_Type(DisplayString):
    """Custom type ruckusZDClientIsolationWhiteListDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_RuckusZDClientIsolationWhiteListDescription_Type.__name__ = "DisplayString"
_RuckusZDClientIsolationWhiteListDescription_Object = MibTableColumn
ruckusZDClientIsolationWhiteListDescription = _RuckusZDClientIsolationWhiteListDescription_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 15, 1, 6),
    _RuckusZDClientIsolationWhiteListDescription_Type()
)
ruckusZDClientIsolationWhiteListDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDClientIsolationWhiteListDescription.setStatus("current")
_RuckusZDClientIsolationWhiteListRowStatus_Type = RowStatus
_RuckusZDClientIsolationWhiteListRowStatus_Object = MibTableColumn
ruckusZDClientIsolationWhiteListRowStatus = _RuckusZDClientIsolationWhiteListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 15, 1, 15),
    _RuckusZDClientIsolationWhiteListRowStatus_Type()
)
ruckusZDClientIsolationWhiteListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruckusZDClientIsolationWhiteListRowStatus.setStatus("current")
_RuckusZDClientIsolationWhiteListRuleTable_Object = MibTable
ruckusZDClientIsolationWhiteListRuleTable = _RuckusZDClientIsolationWhiteListRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 16)
)
if mibBuilder.loadTexts:
    ruckusZDClientIsolationWhiteListRuleTable.setStatus("current")
_RuckusZDClientIsolationWhiteListRuleEntry_Object = MibTableRow
ruckusZDClientIsolationWhiteListRuleEntry = _RuckusZDClientIsolationWhiteListRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 16, 1)
)
ruckusZDClientIsolationWhiteListRuleEntry.setIndexNames(
    (0, "RUCKUS-ZD-WLAN-CONFIG-MIB", "ruckusZDClientIsolationWhiteListID"),
    (0, "RUCKUS-ZD-WLAN-CONFIG-MIB", "ruckusZDClientIsolationWhiteListRuleID"),
)
if mibBuilder.loadTexts:
    ruckusZDClientIsolationWhiteListRuleEntry.setStatus("current")


class _RuckusZDClientIsolationWhiteListRuleID_Type(Integer32):
    """Custom type ruckusZDClientIsolationWhiteListRuleID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_RuckusZDClientIsolationWhiteListRuleID_Type.__name__ = "Integer32"
_RuckusZDClientIsolationWhiteListRuleID_Object = MibTableColumn
ruckusZDClientIsolationWhiteListRuleID = _RuckusZDClientIsolationWhiteListRuleID_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 16, 1, 1),
    _RuckusZDClientIsolationWhiteListRuleID_Type()
)
ruckusZDClientIsolationWhiteListRuleID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruckusZDClientIsolationWhiteListRuleID.setStatus("current")


class _RuckusZDClientIsolationWhiteListRuleDescription_Type(DisplayString):
    """Custom type ruckusZDClientIsolationWhiteListRuleDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_RuckusZDClientIsolationWhiteListRuleDescription_Type.__name__ = "DisplayString"
_RuckusZDClientIsolationWhiteListRuleDescription_Object = MibTableColumn
ruckusZDClientIsolationWhiteListRuleDescription = _RuckusZDClientIsolationWhiteListRuleDescription_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 16, 1, 3),
    _RuckusZDClientIsolationWhiteListRuleDescription_Type()
)
ruckusZDClientIsolationWhiteListRuleDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDClientIsolationWhiteListRuleDescription.setStatus("current")


class _RuckusZDClientIsolationWhiteListRuleMac_Type(DisplayString):
    """Custom type ruckusZDClientIsolationWhiteListRuleMac based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 46),
    )


_RuckusZDClientIsolationWhiteListRuleMac_Type.__name__ = "DisplayString"
_RuckusZDClientIsolationWhiteListRuleMac_Object = MibTableColumn
ruckusZDClientIsolationWhiteListRuleMac = _RuckusZDClientIsolationWhiteListRuleMac_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 16, 1, 5),
    _RuckusZDClientIsolationWhiteListRuleMac_Type()
)
ruckusZDClientIsolationWhiteListRuleMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDClientIsolationWhiteListRuleMac.setStatus("current")


class _RuckusZDClientIsolationWhiteListRuleDesAddr_Type(DisplayString):
    """Custom type ruckusZDClientIsolationWhiteListRuleDesAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 46),
    )


_RuckusZDClientIsolationWhiteListRuleDesAddr_Type.__name__ = "DisplayString"
_RuckusZDClientIsolationWhiteListRuleDesAddr_Object = MibTableColumn
ruckusZDClientIsolationWhiteListRuleDesAddr = _RuckusZDClientIsolationWhiteListRuleDesAddr_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 16, 1, 6),
    _RuckusZDClientIsolationWhiteListRuleDesAddr_Type()
)
ruckusZDClientIsolationWhiteListRuleDesAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDClientIsolationWhiteListRuleDesAddr.setStatus("current")
_RuckusZDClientIsolationWhiteListRuleRowStatus_Type = RowStatus
_RuckusZDClientIsolationWhiteListRuleRowStatus_Object = MibTableColumn
ruckusZDClientIsolationWhiteListRuleRowStatus = _RuckusZDClientIsolationWhiteListRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 16, 1, 10),
    _RuckusZDClientIsolationWhiteListRuleRowStatus_Type()
)
ruckusZDClientIsolationWhiteListRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruckusZDClientIsolationWhiteListRuleRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUCKUS-ZD-WLAN-CONFIG-MIB",
    **{"ruckusZDWLANConfigMIB": ruckusZDWLANConfigMIB,
       "ruckusZDWLANConfigObjects": ruckusZDWLANConfigObjects,
       "ruckusZDWLANConfig": ruckusZDWLANConfig,
       "ruckusZDWLANConfigTable": ruckusZDWLANConfigTable,
       "ruckusZDWLANConfigEntry": ruckusZDWLANConfigEntry,
       "ruckusZDWLANID": ruckusZDWLANID,
       "ruckusZDWLANConfigSSID": ruckusZDWLANConfigSSID,
       "ruckusZDWLANConfigDescription": ruckusZDWLANConfigDescription,
       "ruckusZDWLANConfigName": ruckusZDWLANConfigName,
       "ruckusZDWLANConfigWLANServiceType": ruckusZDWLANConfigWLANServiceType,
       "ruckusZDWLANConfigAuthentication": ruckusZDWLANConfigAuthentication,
       "ruckusZDWLANConfigEncryption": ruckusZDWLANConfigEncryption,
       "ruckusZDWLANConfigWEPKeyIndex": ruckusZDWLANConfigWEPKeyIndex,
       "ruckusZDWLANConfigWEPKey": ruckusZDWLANConfigWEPKey,
       "ruckusZDWLANConfigWPACipherType": ruckusZDWLANConfigWPACipherType,
       "ruckusZDWLANConfigWPAKey": ruckusZDWLANConfigWPAKey,
       "ruckusZDWLANConfigAuthenticationServerID": ruckusZDWLANConfigAuthenticationServerID,
       "ruckusZDWLANConfigWirelessClientIsolation": ruckusZDWLANConfigWirelessClientIsolation,
       "ruckusZDWLANConfigWirelessWhiteListID": ruckusZDWLANConfigWirelessWhiteListID,
       "ruckusZDWLANConfigZeroITActivation": ruckusZDWLANConfigZeroITActivation,
       "ruckusZDWLANConfigWLANHotspotID": ruckusZDWLANConfigWLANHotspotID,
       "ruckusZDWLANConfigWLANServicePriority": ruckusZDWLANConfigWLANServicePriority,
       "ruckusZDWLANConfigAccountingServerID": ruckusZDWLANConfigAccountingServerID,
       "ruckusZDWLANConfigAccountingUpdateInterval": ruckusZDWLANConfigAccountingUpdateInterval,
       "ruckusZDWLANConfigUplinkRate": ruckusZDWLANConfigUplinkRate,
       "ruckusZDWLANConfigDownlinkRate": ruckusZDWLANConfigDownlinkRate,
       "ruckusZDWLANConfigIGMPSnooping": ruckusZDWLANConfigIGMPSnooping,
       "ruckusZDWLANConfigVlanID": ruckusZDWLANConfigVlanID,
       "ruckusZDWLANConfigDynamicVLAN": ruckusZDWLANConfigDynamicVLAN,
       "ruckusZDWLANConfigHideSSID": ruckusZDWLANConfigHideSSID,
       "ruckusZDWLANConfigTunnelMode": ruckusZDWLANConfigTunnelMode,
       "ruckusZDWLANConfigBackgroundScanning": ruckusZDWLANConfigBackgroundScanning,
       "ruckusZDWLANConfigMaxClients": ruckusZDWLANConfigMaxClients,
       "ruckusZDWLANConfigWebAuthentication": ruckusZDWLANConfigWebAuthentication,
       "ruckusZDWLANConfigRowStatus": ruckusZDWLANConfigRowStatus,
       "ruckusZDWLANGroupConfigTable": ruckusZDWLANGroupConfigTable,
       "ruckusZDWLANGroupConfigEntry": ruckusZDWLANGroupConfigEntry,
       "ruckusZDWLANGroupID": ruckusZDWLANGroupID,
       "ruckusZDWLANGroupConfigName": ruckusZDWLANGroupConfigName,
       "ruckusZDWLANGroupConfigDescription": ruckusZDWLANGroupConfigDescription,
       "ruckusZDWLANGroupVlanOverrideStatus": ruckusZDWLANGroupVlanOverrideStatus,
       "ruckusZDWLANGroupConfigRowStatus": ruckusZDWLANGroupConfigRowStatus,
       "ruckusZDWLANGroupCfgAttrTable": ruckusZDWLANGroupCfgAttrTable,
       "ruckusZDWLANGroupCfgAttrEntry": ruckusZDWLANGroupCfgAttrEntry,
       "ruckusZDWLANGroupCfgAttrOverrideType": ruckusZDWLANGroupCfgAttrOverrideType,
       "ruckusZDWLANGroupCfgAttrWGVlanTag": ruckusZDWLANGroupCfgAttrWGVlanTag,
       "ruckusZDWLANGroupCfgAttrRowStatus": ruckusZDWLANGroupCfgAttrRowStatus,
       "ruckusZDHotspotConfigTable": ruckusZDHotspotConfigTable,
       "ruckusZDHotspotConfigEntry": ruckusZDHotspotConfigEntry,
       "ruckusZDHotspotID": ruckusZDHotspotID,
       "ruckusZDHotspotName": ruckusZDHotspotName,
       "ruckusZDHotspotRedirectLoginPage": ruckusZDHotspotRedirectLoginPage,
       "ruckusZDHotspotRedirectStartURL": ruckusZDHotspotRedirectStartURL,
       "ruckusZDHotspotRedirectType": ruckusZDHotspotRedirectType,
       "ruckusZDHotspotRowStatus": ruckusZDHotspotRowStatus,
       "ruckusZDClientIsolationWhiteListTable": ruckusZDClientIsolationWhiteListTable,
       "ruckusZDClientIsolationWhiteListEntry": ruckusZDClientIsolationWhiteListEntry,
       "ruckusZDClientIsolationWhiteListID": ruckusZDClientIsolationWhiteListID,
       "ruckusZDClientIsolationWhiteListName": ruckusZDClientIsolationWhiteListName,
       "ruckusZDClientIsolationWhiteListDescription": ruckusZDClientIsolationWhiteListDescription,
       "ruckusZDClientIsolationWhiteListRowStatus": ruckusZDClientIsolationWhiteListRowStatus,
       "ruckusZDClientIsolationWhiteListRuleTable": ruckusZDClientIsolationWhiteListRuleTable,
       "ruckusZDClientIsolationWhiteListRuleEntry": ruckusZDClientIsolationWhiteListRuleEntry,
       "ruckusZDClientIsolationWhiteListRuleID": ruckusZDClientIsolationWhiteListRuleID,
       "ruckusZDClientIsolationWhiteListRuleDescription": ruckusZDClientIsolationWhiteListRuleDescription,
       "ruckusZDClientIsolationWhiteListRuleMac": ruckusZDClientIsolationWhiteListRuleMac,
       "ruckusZDClientIsolationWhiteListRuleDesAddr": ruckusZDClientIsolationWhiteListRuleDesAddr,
       "ruckusZDClientIsolationWhiteListRuleRowStatus": ruckusZDClientIsolationWhiteListRuleRowStatus}
)
