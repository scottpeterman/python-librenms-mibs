# SNMP MIB module (RUCKUS-SZ-CONFIG-WLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ruckus\RUCKUS-SZ-CONFIG-WLAN-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:23:46 2025
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

(IANAifType,) = mibBuilder.importSymbols(
    "IANAifType-MIB",
    "IANAifType")

(Ipv6Address,) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address")

(ruckusSZWLANModule,) = mibBuilder.importSymbols(
    "RUCKUS-ROOT-MIB",
    "ruckusSZWLANModule")

(RuckusAdminStatus,
 RuckusRadioMode,
 RuckusRateLimiting,
 RuckusSSID,
 RuckusdB) = mibBuilder.importSymbols(
    "RUCKUS-TC-MIB",
    "RuckusAdminStatus",
    "RuckusRadioMode",
    "RuckusRateLimiting",
    "RuckusSSID",
    "RuckusdB")

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

ruckusSZConfigWLANMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 4, 2, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuckusSZConfigWLANObjects_ObjectIdentity = ObjectIdentity
ruckusSZConfigWLANObjects = _RuckusSZConfigWLANObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 4, 2, 2, 1)
)
_RuckusSZConfigWLAN_ObjectIdentity = ObjectIdentity
ruckusSZConfigWLAN = _RuckusSZConfigWLAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 4, 2, 2, 1, 1)
)
_RuckusSZConfigWLANTable_Object = MibTable
ruckusSZConfigWLANTable = _RuckusSZConfigWLANTable_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 4, 2, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ruckusSZConfigWLANTable.setStatus("current")
_RuckusSZConfigWLANEntry_Object = MibTableRow
ruckusSZConfigWLANEntry = _RuckusSZConfigWLANEntry_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 4, 2, 2, 1, 1, 1, 1)
)
ruckusSZConfigWLANEntry.setIndexNames(
    (0, "RUCKUS-SZ-CONFIG-WLAN-MIB", "ruckusSZConfigWLANID"),
)
if mibBuilder.loadTexts:
    ruckusSZConfigWLANEntry.setStatus("current")


class _RuckusSZConfigWLANID_Type(Integer32):
    """Custom type ruckusSZConfigWLANID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RuckusSZConfigWLANID_Type.__name__ = "Integer32"
_RuckusSZConfigWLANID_Object = MibTableColumn
ruckusSZConfigWLANID = _RuckusSZConfigWLANID_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 4, 2, 2, 1, 1, 1, 1, 1),
    _RuckusSZConfigWLANID_Type()
)
ruckusSZConfigWLANID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSZConfigWLANID.setStatus("current")


class _RuckusSZConfigWLANSSID_Type(OctetString):
    """Custom type ruckusSZConfigWLANSSID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 32),
    )


_RuckusSZConfigWLANSSID_Type.__name__ = "OctetString"
_RuckusSZConfigWLANSSID_Object = MibTableColumn
ruckusSZConfigWLANSSID = _RuckusSZConfigWLANSSID_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 4, 2, 2, 1, 1, 1, 1, 2),
    _RuckusSZConfigWLANSSID_Type()
)
ruckusSZConfigWLANSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSZConfigWLANSSID.setStatus("current")


class _RuckusSZConfigWLANDescription_Type(DisplayString):
    """Custom type ruckusSZConfigWLANDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_RuckusSZConfigWLANDescription_Type.__name__ = "DisplayString"
_RuckusSZConfigWLANDescription_Object = MibTableColumn
ruckusSZConfigWLANDescription = _RuckusSZConfigWLANDescription_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 4, 2, 2, 1, 1, 1, 1, 3),
    _RuckusSZConfigWLANDescription_Type()
)
ruckusSZConfigWLANDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusSZConfigWLANDescription.setStatus("current")


class _RuckusSZConfigWLANName_Type(OctetString):
    """Custom type ruckusSZConfigWLANName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 32),
    )


_RuckusSZConfigWLANName_Type.__name__ = "OctetString"
_RuckusSZConfigWLANName_Object = MibTableColumn
ruckusSZConfigWLANName = _RuckusSZConfigWLANName_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 4, 2, 2, 1, 1, 1, 1, 4),
    _RuckusSZConfigWLANName_Type()
)
ruckusSZConfigWLANName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSZConfigWLANName.setStatus("current")


class _RuckusSZConfigWLANWLANServiceType_Type(Integer32):
    """Custom type ruckusSZConfigWLANWLANServiceType based on Integer32"""
    defaultValue = 1

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
        *(("standardUsage", 1),
          ("hotspot", 2),
          ("guest", 3),
          ("webauth", 4),
          ("hotspot20", 5),
          ("hotspot20-osen", 6))
    )


_RuckusSZConfigWLANWLANServiceType_Type.__name__ = "Integer32"
_RuckusSZConfigWLANWLANServiceType_Object = MibTableColumn
ruckusSZConfigWLANWLANServiceType = _RuckusSZConfigWLANWLANServiceType_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 4, 2, 2, 1, 1, 1, 1, 8),
    _RuckusSZConfigWLANWLANServiceType_Type()
)
ruckusSZConfigWLANWLANServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSZConfigWLANWLANServiceType.setStatus("current")


class _RuckusSZConfigWLANAuthentication_Type(Integer32):
    """Custom type ruckusSZConfigWLANAuthentication based on Integer32"""
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
        *(("open", 1),
          ("eap", 2),
          ("mac-address", 3))
    )


_RuckusSZConfigWLANAuthentication_Type.__name__ = "Integer32"
_RuckusSZConfigWLANAuthentication_Object = MibTableColumn
ruckusSZConfigWLANAuthentication = _RuckusSZConfigWLANAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 4, 2, 2, 1, 1, 1, 1, 10),
    _RuckusSZConfigWLANAuthentication_Type()
)
ruckusSZConfigWLANAuthentication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSZConfigWLANAuthentication.setStatus("current")


class _RuckusSZConfigWLANEncryption_Type(Integer32):
    """Custom type ruckusSZConfigWLANEncryption based on Integer32"""
    defaultValue = 5

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
        *(("wpa2", 1),
          ("wpa-Mixed", 2),
          ("wep-64", 3),
          ("wep-128", 4),
          ("none-enc", 5))
    )


_RuckusSZConfigWLANEncryption_Type.__name__ = "Integer32"
_RuckusSZConfigWLANEncryption_Object = MibTableColumn
ruckusSZConfigWLANEncryption = _RuckusSZConfigWLANEncryption_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 4, 2, 2, 1, 1, 1, 1, 12),
    _RuckusSZConfigWLANEncryption_Type()
)
ruckusSZConfigWLANEncryption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusSZConfigWLANEncryption.setStatus("current")


class _RuckusSZConfigWLANWEPKeyIndex_Type(Integer32):
    """Custom type ruckusSZConfigWLANWEPKeyIndex based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_RuckusSZConfigWLANWEPKeyIndex_Type.__name__ = "Integer32"
_RuckusSZConfigWLANWEPKeyIndex_Object = MibTableColumn
ruckusSZConfigWLANWEPKeyIndex = _RuckusSZConfigWLANWEPKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 4, 2, 2, 1, 1, 1, 1, 15),
    _RuckusSZConfigWLANWEPKeyIndex_Type()
)
ruckusSZConfigWLANWEPKeyIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusSZConfigWLANWEPKeyIndex.setStatus("current")


class _RuckusSZConfigWLANWEPKey_Type(OctetString):
    """Custom type ruckusSZConfigWLANWEPKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
        ValueSizeConstraint(26, 26),
    )


_RuckusSZConfigWLANWEPKey_Type.__name__ = "OctetString"
_RuckusSZConfigWLANWEPKey_Object = MibTableColumn
ruckusSZConfigWLANWEPKey = _RuckusSZConfigWLANWEPKey_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 4, 2, 2, 1, 1, 1, 1, 16),
    _RuckusSZConfigWLANWEPKey_Type()
)
ruckusSZConfigWLANWEPKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusSZConfigWLANWEPKey.setStatus("current")


class _RuckusSZConfigWLANWPACipherType_Type(Integer32):
    """Custom type ruckusSZConfigWLANWPACipherType based on Integer32"""
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
        *(("aes", 1),
          ("tkipaes", 2),
          ("null", 3))
    )


_RuckusSZConfigWLANWPACipherType_Type.__name__ = "Integer32"
_RuckusSZConfigWLANWPACipherType_Object = MibTableColumn
ruckusSZConfigWLANWPACipherType = _RuckusSZConfigWLANWPACipherType_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 4, 2, 2, 1, 1, 1, 1, 20),
    _RuckusSZConfigWLANWPACipherType_Type()
)
ruckusSZConfigWLANWPACipherType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusSZConfigWLANWPACipherType.setStatus("current")


class _RuckusSZConfigWLANWPAKey_Type(OctetString):
    """Custom type ruckusSZConfigWLANWPAKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 63),
        ValueSizeConstraint(64, 64),
    )


_RuckusSZConfigWLANWPAKey_Type.__name__ = "OctetString"
_RuckusSZConfigWLANWPAKey_Object = MibTableColumn
ruckusSZConfigWLANWPAKey = _RuckusSZConfigWLANWPAKey_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 4, 2, 2, 1, 1, 1, 1, 21),
    _RuckusSZConfigWLANWPAKey_Type()
)
ruckusSZConfigWLANWPAKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusSZConfigWLANWPAKey.setStatus("current")


class _RuckusSZConfigWLANWirelessClientIsolation_Type(Integer32):
    """Custom type ruckusSZConfigWLANWirelessClientIsolation based on Integer32"""
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


_RuckusSZConfigWLANWirelessClientIsolation_Type.__name__ = "Integer32"
_RuckusSZConfigWLANWirelessClientIsolation_Object = MibTableColumn
ruckusSZConfigWLANWirelessClientIsolation = _RuckusSZConfigWLANWirelessClientIsolation_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 4, 2, 2, 1, 1, 1, 1, 28),
    _RuckusSZConfigWLANWirelessClientIsolation_Type()
)
ruckusSZConfigWLANWirelessClientIsolation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusSZConfigWLANWirelessClientIsolation.setStatus("current")


class _RuckusSZConfigWLANZeroITActivation_Type(Integer32):
    """Custom type ruckusSZConfigWLANZeroITActivation based on Integer32"""
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


_RuckusSZConfigWLANZeroITActivation_Type.__name__ = "Integer32"
_RuckusSZConfigWLANZeroITActivation_Object = MibTableColumn
ruckusSZConfigWLANZeroITActivation = _RuckusSZConfigWLANZeroITActivation_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 4, 2, 2, 1, 1, 1, 1, 30),
    _RuckusSZConfigWLANZeroITActivation_Type()
)
ruckusSZConfigWLANZeroITActivation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusSZConfigWLANZeroITActivation.setStatus("current")


class _RuckusSZConfigWLANServicePriority_Type(Integer32):
    """Custom type ruckusSZConfigWLANServicePriority based on Integer32"""
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


_RuckusSZConfigWLANServicePriority_Type.__name__ = "Integer32"
_RuckusSZConfigWLANServicePriority_Object = MibTableColumn
ruckusSZConfigWLANServicePriority = _RuckusSZConfigWLANServicePriority_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 4, 2, 2, 1, 1, 1, 1, 32),
    _RuckusSZConfigWLANServicePriority_Type()
)
ruckusSZConfigWLANServicePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusSZConfigWLANServicePriority.setStatus("current")


class _RuckusSZConfigWLANAccountingUpdateInterval_Type(Integer32):
    """Custom type ruckusSZConfigWLANAccountingUpdateInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_RuckusSZConfigWLANAccountingUpdateInterval_Type.__name__ = "Integer32"
_RuckusSZConfigWLANAccountingUpdateInterval_Object = MibTableColumn
ruckusSZConfigWLANAccountingUpdateInterval = _RuckusSZConfigWLANAccountingUpdateInterval_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 4, 2, 2, 1, 1, 1, 1, 36),
    _RuckusSZConfigWLANAccountingUpdateInterval_Type()
)
ruckusSZConfigWLANAccountingUpdateInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusSZConfigWLANAccountingUpdateInterval.setStatus("current")


class _RuckusSZConfigWLANVlanID_Type(Integer32):
    """Custom type ruckusSZConfigWLANVlanID based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_RuckusSZConfigWLANVlanID_Type.__name__ = "Integer32"
_RuckusSZConfigWLANVlanID_Object = MibTableColumn
ruckusSZConfigWLANVlanID = _RuckusSZConfigWLANVlanID_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 4, 2, 2, 1, 1, 1, 1, 45),
    _RuckusSZConfigWLANVlanID_Type()
)
ruckusSZConfigWLANVlanID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusSZConfigWLANVlanID.setStatus("current")


class _RuckusSZConfigWLANHideSSID_Type(Integer32):
    """Custom type ruckusSZConfigWLANHideSSID based on Integer32"""
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


_RuckusSZConfigWLANHideSSID_Type.__name__ = "Integer32"
_RuckusSZConfigWLANHideSSID_Object = MibTableColumn
ruckusSZConfigWLANHideSSID = _RuckusSZConfigWLANHideSSID_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 4, 2, 2, 1, 1, 1, 1, 50),
    _RuckusSZConfigWLANHideSSID_Type()
)
ruckusSZConfigWLANHideSSID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusSZConfigWLANHideSSID.setStatus("current")


class _RuckusSZConfigWLANMaxClientsPerAP_Type(Integer32):
    """Custom type ruckusSZConfigWLANMaxClientsPerAP based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_RuckusSZConfigWLANMaxClientsPerAP_Type.__name__ = "Integer32"
_RuckusSZConfigWLANMaxClientsPerAP_Object = MibTableColumn
ruckusSZConfigWLANMaxClientsPerAP = _RuckusSZConfigWLANMaxClientsPerAP_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 4, 2, 2, 1, 1, 1, 1, 55),
    _RuckusSZConfigWLANMaxClientsPerAP_Type()
)
ruckusSZConfigWLANMaxClientsPerAP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusSZConfigWLANMaxClientsPerAP.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUCKUS-SZ-CONFIG-WLAN-MIB",
    **{"ruckusSZConfigWLANMIB": ruckusSZConfigWLANMIB,
       "ruckusSZConfigWLANObjects": ruckusSZConfigWLANObjects,
       "ruckusSZConfigWLAN": ruckusSZConfigWLAN,
       "ruckusSZConfigWLANTable": ruckusSZConfigWLANTable,
       "ruckusSZConfigWLANEntry": ruckusSZConfigWLANEntry,
       "ruckusSZConfigWLANID": ruckusSZConfigWLANID,
       "ruckusSZConfigWLANSSID": ruckusSZConfigWLANSSID,
       "ruckusSZConfigWLANDescription": ruckusSZConfigWLANDescription,
       "ruckusSZConfigWLANName": ruckusSZConfigWLANName,
       "ruckusSZConfigWLANWLANServiceType": ruckusSZConfigWLANWLANServiceType,
       "ruckusSZConfigWLANAuthentication": ruckusSZConfigWLANAuthentication,
       "ruckusSZConfigWLANEncryption": ruckusSZConfigWLANEncryption,
       "ruckusSZConfigWLANWEPKeyIndex": ruckusSZConfigWLANWEPKeyIndex,
       "ruckusSZConfigWLANWEPKey": ruckusSZConfigWLANWEPKey,
       "ruckusSZConfigWLANWPACipherType": ruckusSZConfigWLANWPACipherType,
       "ruckusSZConfigWLANWPAKey": ruckusSZConfigWLANWPAKey,
       "ruckusSZConfigWLANWirelessClientIsolation": ruckusSZConfigWLANWirelessClientIsolation,
       "ruckusSZConfigWLANZeroITActivation": ruckusSZConfigWLANZeroITActivation,
       "ruckusSZConfigWLANServicePriority": ruckusSZConfigWLANServicePriority,
       "ruckusSZConfigWLANAccountingUpdateInterval": ruckusSZConfigWLANAccountingUpdateInterval,
       "ruckusSZConfigWLANVlanID": ruckusSZConfigWLANVlanID,
       "ruckusSZConfigWLANHideSSID": ruckusSZConfigWLANHideSSID,
       "ruckusSZConfigWLANMaxClientsPerAP": ruckusSZConfigWLANMaxClientsPerAP}
)
