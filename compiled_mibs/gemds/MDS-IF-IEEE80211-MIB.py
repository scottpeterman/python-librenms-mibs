# SNMP MIB module (MDS-IF-IEEE80211-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\gemds\MDS-IF-IEEE80211-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:47:25 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(mdsInterfaces,) = mibBuilder.importSymbols(
    "MDS-ORBIT-SMI-MIB",
    "mdsInterfaces")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

mdsIfDot11MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 2)
)
if mibBuilder.loadTexts:
    mdsIfDot11MIB.setRevisions(
        ("2018-05-16 00:00",
         "2014-10-20 00:00",
         "2013-04-26 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class Byte(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )



class UnsignedByte(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class UnsignedShort(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class Ssid(TextualConvention, OctetString):
    status = "current"
    displayHint = "32a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )



class MacString(TextualConvention, OctetString):
    status = "current"
    displayHint = "20a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )



# MIB Managed Objects in the order of their OIDs

_MIfDot11MIBObjects_ObjectIdentity = ObjectIdentity
mIfDot11MIBObjects = _MIfDot11MIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 1)
)
_MIfDot11Config_ObjectIdentity = ObjectIdentity
mIfDot11Config = _MIfDot11Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 1, 1)
)
_MIfDot11Status_ObjectIdentity = ObjectIdentity
mIfDot11Status = _MIfDot11Status_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 1, 2)
)
_MIfDot11StatusTable_Object = MibTable
mIfDot11StatusTable = _MIfDot11StatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    mIfDot11StatusTable.setStatus("current")
_MIfDot11StatusEntry_Object = MibTableRow
mIfDot11StatusEntry = _MIfDot11StatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 1, 2, 1, 1)
)
mIfDot11StatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    mIfDot11StatusEntry.setStatus("current")
_MIfDot11SerialNumber_Type = DisplayString
_MIfDot11SerialNumber_Object = MibTableColumn
mIfDot11SerialNumber = _MIfDot11SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 1, 2, 1, 1, 1),
    _MIfDot11SerialNumber_Type()
)
mIfDot11SerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfDot11SerialNumber.setStatus("current")


class _MIfDot11Mode_Type(Integer32):
    """Custom type mIfDot11Mode based on Integer32"""
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
        *(("unknown", 0),
          ("station", 1),
          ("accessPoint", 2),
          ("accessPointStation", 3))
    )


_MIfDot11Mode_Type.__name__ = "Integer32"
_MIfDot11Mode_Object = MibTableColumn
mIfDot11Mode = _MIfDot11Mode_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 1, 2, 1, 1, 2),
    _MIfDot11Mode_Type()
)
mIfDot11Mode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfDot11Mode.setStatus("current")
_MIfDot11TxPower_Type = UnsignedByte
_MIfDot11TxPower_Object = MibTableColumn
mIfDot11TxPower = _MIfDot11TxPower_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 1, 2, 1, 1, 3),
    _MIfDot11TxPower_Type()
)
mIfDot11TxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfDot11TxPower.setStatus("current")
_MIfDot11Channel_Type = UnsignedByte
_MIfDot11Channel_Object = MibTableColumn
mIfDot11Channel = _MIfDot11Channel_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 1, 2, 1, 1, 4),
    _MIfDot11Channel_Type()
)
mIfDot11Channel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfDot11Channel.setStatus("current")
_MIfDot11StationSsid_Type = Ssid
_MIfDot11StationSsid_Object = MibTableColumn
mIfDot11StationSsid = _MIfDot11StationSsid_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 1, 2, 1, 1, 5),
    _MIfDot11StationSsid_Type()
)
mIfDot11StationSsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfDot11StationSsid.setStatus("current")
_MIfDot11StationBssid_Type = MacString
_MIfDot11StationBssid_Object = MibTableColumn
mIfDot11StationBssid = _MIfDot11StationBssid_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 1, 2, 1, 1, 6),
    _MIfDot11StationBssid_Type()
)
mIfDot11StationBssid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfDot11StationBssid.setStatus("current")
_MIfDot11StationRssi_Type = Byte
_MIfDot11StationRssi_Object = MibTableColumn
mIfDot11StationRssi = _MIfDot11StationRssi_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 1, 2, 1, 1, 7),
    _MIfDot11StationRssi_Type()
)
mIfDot11StationRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfDot11StationRssi.setStatus("current")
_MIfDot11StationAuthenticated_Type = TruthValue
_MIfDot11StationAuthenticated_Object = MibTableColumn
mIfDot11StationAuthenticated = _MIfDot11StationAuthenticated_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 1, 2, 1, 1, 8),
    _MIfDot11StationAuthenticated_Type()
)
mIfDot11StationAuthenticated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfDot11StationAuthenticated.setStatus("current")
_MIfDot11StationAuthorized_Type = TruthValue
_MIfDot11StationAuthorized_Object = MibTableColumn
mIfDot11StationAuthorized = _MIfDot11StationAuthorized_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 1, 2, 1, 1, 9),
    _MIfDot11StationAuthorized_Type()
)
mIfDot11StationAuthorized.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfDot11StationAuthorized.setStatus("current")
_MIfDot11StationInactive_Type = Unsigned32
_MIfDot11StationInactive_Object = MibTableColumn
mIfDot11StationInactive = _MIfDot11StationInactive_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 1, 2, 1, 1, 10),
    _MIfDot11StationInactive_Type()
)
mIfDot11StationInactive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfDot11StationInactive.setStatus("current")
_MIfDot11StationRxbytes_Type = Unsigned32
_MIfDot11StationRxbytes_Object = MibTableColumn
mIfDot11StationRxbytes = _MIfDot11StationRxbytes_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 1, 2, 1, 1, 11),
    _MIfDot11StationRxbytes_Type()
)
mIfDot11StationRxbytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfDot11StationRxbytes.setStatus("current")
_MIfDot11StationRxpackets_Type = Unsigned32
_MIfDot11StationRxpackets_Object = MibTableColumn
mIfDot11StationRxpackets = _MIfDot11StationRxpackets_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 1, 2, 1, 1, 12),
    _MIfDot11StationRxpackets_Type()
)
mIfDot11StationRxpackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfDot11StationRxpackets.setStatus("current")
_MIfDot11StationTxbitrate_Type = UnsignedShort
_MIfDot11StationTxbitrate_Object = MibTableColumn
mIfDot11StationTxbitrate = _MIfDot11StationTxbitrate_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 1, 2, 1, 1, 13),
    _MIfDot11StationTxbitrate_Type()
)
mIfDot11StationTxbitrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfDot11StationTxbitrate.setStatus("current")
_MIfDot11StationTxbytes_Type = Unsigned32
_MIfDot11StationTxbytes_Object = MibTableColumn
mIfDot11StationTxbytes = _MIfDot11StationTxbytes_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 1, 2, 1, 1, 14),
    _MIfDot11StationTxbytes_Type()
)
mIfDot11StationTxbytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfDot11StationTxbytes.setStatus("current")
_MIfDot11StationTxpackets_Type = Unsigned32
_MIfDot11StationTxpackets_Object = MibTableColumn
mIfDot11StationTxpackets = _MIfDot11StationTxpackets_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 1, 2, 1, 1, 15),
    _MIfDot11StationTxpackets_Type()
)
mIfDot11StationTxpackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfDot11StationTxpackets.setStatus("current")
_MIfDot11StationTxfailed_Type = Unsigned32
_MIfDot11StationTxfailed_Object = MibTableColumn
mIfDot11StationTxfailed = _MIfDot11StationTxfailed_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 1, 2, 1, 1, 16),
    _MIfDot11StationTxfailed_Type()
)
mIfDot11StationTxfailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfDot11StationTxfailed.setStatus("current")
_MIfDot11StationTxretries_Type = Unsigned32
_MIfDot11StationTxretries_Object = MibTableColumn
mIfDot11StationTxretries = _MIfDot11StationTxretries_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 1, 2, 1, 1, 17),
    _MIfDot11StationTxretries_Type()
)
mIfDot11StationTxretries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfDot11StationTxretries.setStatus("current")


class _MIfDot11ModemType_Type(Integer32):
    """Custom type mIfDot11ModemType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("w51", 1),
          ("w52", 2))
    )


_MIfDot11ModemType_Type.__name__ = "Integer32"
_MIfDot11ModemType_Object = MibTableColumn
mIfDot11ModemType = _MIfDot11ModemType_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 1, 2, 1, 1, 18),
    _MIfDot11ModemType_Type()
)
mIfDot11ModemType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfDot11ModemType.setStatus("current")
_MIfDot11StatusApTable_Object = MibTable
mIfDot11StatusApTable = _MIfDot11StatusApTable_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 1, 2, 2)
)
if mibBuilder.loadTexts:
    mIfDot11StatusApTable.setStatus("current")
_MIfDot11StatusApEntry_Object = MibTableRow
mIfDot11StatusApEntry = _MIfDot11StatusApEntry_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 1, 2, 2, 1)
)
mIfDot11StatusApEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "MDS-IF-IEEE80211-MIB", "mIfDot11ApSsid"),
)
if mibBuilder.loadTexts:
    mIfDot11StatusApEntry.setStatus("current")
_MIfDot11ApSsid_Type = Ssid
_MIfDot11ApSsid_Object = MibTableColumn
mIfDot11ApSsid = _MIfDot11ApSsid_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 1, 2, 2, 1, 1),
    _MIfDot11ApSsid_Type()
)
mIfDot11ApSsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfDot11ApSsid.setStatus("current")
_MIfDot11StatusApClientTable_Object = MibTable
mIfDot11StatusApClientTable = _MIfDot11StatusApClientTable_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 1, 2, 3)
)
if mibBuilder.loadTexts:
    mIfDot11StatusApClientTable.setStatus("current")
_MIfDot11StatusApClientEntry_Object = MibTableRow
mIfDot11StatusApClientEntry = _MIfDot11StatusApClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 1, 2, 3, 1)
)
mIfDot11StatusApClientEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "MDS-IF-IEEE80211-MIB", "mIfDot11ApSsid"),
    (0, "MDS-IF-IEEE80211-MIB", "mIfDot11ApClientMac"),
)
if mibBuilder.loadTexts:
    mIfDot11StatusApClientEntry.setStatus("current")
_MIfDot11ApClientMac_Type = MacString
_MIfDot11ApClientMac_Object = MibTableColumn
mIfDot11ApClientMac = _MIfDot11ApClientMac_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 1, 2, 3, 1, 1),
    _MIfDot11ApClientMac_Type()
)
mIfDot11ApClientMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfDot11ApClientMac.setStatus("current")
_MIfDot11ApClientRssi_Type = Byte
_MIfDot11ApClientRssi_Object = MibTableColumn
mIfDot11ApClientRssi = _MIfDot11ApClientRssi_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 1, 2, 3, 1, 2),
    _MIfDot11ApClientRssi_Type()
)
mIfDot11ApClientRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfDot11ApClientRssi.setStatus("current")
_MIfDot11ApClientAuthenticated_Type = TruthValue
_MIfDot11ApClientAuthenticated_Object = MibTableColumn
mIfDot11ApClientAuthenticated = _MIfDot11ApClientAuthenticated_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 1, 2, 3, 1, 3),
    _MIfDot11ApClientAuthenticated_Type()
)
mIfDot11ApClientAuthenticated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfDot11ApClientAuthenticated.setStatus("current")
_MIfDot11ApClientAuthorized_Type = TruthValue
_MIfDot11ApClientAuthorized_Object = MibTableColumn
mIfDot11ApClientAuthorized = _MIfDot11ApClientAuthorized_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 1, 2, 3, 1, 4),
    _MIfDot11ApClientAuthorized_Type()
)
mIfDot11ApClientAuthorized.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfDot11ApClientAuthorized.setStatus("current")
_MIfDot11ApClientInactive_Type = Unsigned32
_MIfDot11ApClientInactive_Object = MibTableColumn
mIfDot11ApClientInactive = _MIfDot11ApClientInactive_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 1, 2, 3, 1, 5),
    _MIfDot11ApClientInactive_Type()
)
mIfDot11ApClientInactive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfDot11ApClientInactive.setStatus("current")
_MIfDot11ApClientRxbytes_Type = Unsigned32
_MIfDot11ApClientRxbytes_Object = MibTableColumn
mIfDot11ApClientRxbytes = _MIfDot11ApClientRxbytes_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 1, 2, 3, 1, 6),
    _MIfDot11ApClientRxbytes_Type()
)
mIfDot11ApClientRxbytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfDot11ApClientRxbytes.setStatus("current")
_MIfDot11ApClientRxpackets_Type = Unsigned32
_MIfDot11ApClientRxpackets_Object = MibTableColumn
mIfDot11ApClientRxpackets = _MIfDot11ApClientRxpackets_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 1, 2, 3, 1, 7),
    _MIfDot11ApClientRxpackets_Type()
)
mIfDot11ApClientRxpackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfDot11ApClientRxpackets.setStatus("current")
_MIfDot11ApClientTxbitrate_Type = UnsignedShort
_MIfDot11ApClientTxbitrate_Object = MibTableColumn
mIfDot11ApClientTxbitrate = _MIfDot11ApClientTxbitrate_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 1, 2, 3, 1, 8),
    _MIfDot11ApClientTxbitrate_Type()
)
mIfDot11ApClientTxbitrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfDot11ApClientTxbitrate.setStatus("current")
_MIfDot11ApClientTxbytes_Type = Unsigned32
_MIfDot11ApClientTxbytes_Object = MibTableColumn
mIfDot11ApClientTxbytes = _MIfDot11ApClientTxbytes_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 1, 2, 3, 1, 9),
    _MIfDot11ApClientTxbytes_Type()
)
mIfDot11ApClientTxbytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfDot11ApClientTxbytes.setStatus("current")
_MIfDot11ApClientTxpackets_Type = Unsigned32
_MIfDot11ApClientTxpackets_Object = MibTableColumn
mIfDot11ApClientTxpackets = _MIfDot11ApClientTxpackets_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 1, 2, 3, 1, 10),
    _MIfDot11ApClientTxpackets_Type()
)
mIfDot11ApClientTxpackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfDot11ApClientTxpackets.setStatus("current")
_MIfDot11ApClientTxfailed_Type = Unsigned32
_MIfDot11ApClientTxfailed_Object = MibTableColumn
mIfDot11ApClientTxfailed = _MIfDot11ApClientTxfailed_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 1, 2, 3, 1, 11),
    _MIfDot11ApClientTxfailed_Type()
)
mIfDot11ApClientTxfailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfDot11ApClientTxfailed.setStatus("current")
_MIfDot11ApClientTxretries_Type = Unsigned32
_MIfDot11ApClientTxretries_Object = MibTableColumn
mIfDot11ApClientTxretries = _MIfDot11ApClientTxretries_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 1, 2, 3, 1, 12),
    _MIfDot11ApClientTxretries_Type()
)
mIfDot11ApClientTxretries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfDot11ApClientTxretries.setStatus("current")
_MdsIfDot11MIBConformance_ObjectIdentity = ObjectIdentity
mdsIfDot11MIBConformance = _MdsIfDot11MIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 3)
)
_MdsIfDot11MIBCompliances_ObjectIdentity = ObjectIdentity
mdsIfDot11MIBCompliances = _MdsIfDot11MIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 3, 1)
)
_MdsIfDot11MIBGroups_ObjectIdentity = ObjectIdentity
mdsIfDot11MIBGroups = _MdsIfDot11MIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 3, 2)
)

# Managed Objects groups

mIfDot11StatusCommonGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 3, 2, 1)
)
mIfDot11StatusCommonGroup.setObjects(
      *(("MDS-IF-IEEE80211-MIB", "mIfDot11SerialNumber"),
        ("MDS-IF-IEEE80211-MIB", "mIfDot11Mode"),
        ("MDS-IF-IEEE80211-MIB", "mIfDot11TxPower"),
        ("MDS-IF-IEEE80211-MIB", "mIfDot11Channel"),
        ("MDS-IF-IEEE80211-MIB", "mIfDot11ModemType"))
)
if mibBuilder.loadTexts:
    mIfDot11StatusCommonGroup.setStatus("current")

mIfDot11StatusStationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 3, 2, 2)
)
mIfDot11StatusStationGroup.setObjects(
      *(("MDS-IF-IEEE80211-MIB", "mIfDot11StationSsid"),
        ("MDS-IF-IEEE80211-MIB", "mIfDot11StationRssi"),
        ("MDS-IF-IEEE80211-MIB", "mIfDot11StationBssid"),
        ("MDS-IF-IEEE80211-MIB", "mIfDot11StationAuthenticated"),
        ("MDS-IF-IEEE80211-MIB", "mIfDot11StationAuthorized"),
        ("MDS-IF-IEEE80211-MIB", "mIfDot11StationInactive"),
        ("MDS-IF-IEEE80211-MIB", "mIfDot11StationRxbytes"),
        ("MDS-IF-IEEE80211-MIB", "mIfDot11StationRxpackets"),
        ("MDS-IF-IEEE80211-MIB", "mIfDot11StationTxbitrate"),
        ("MDS-IF-IEEE80211-MIB", "mIfDot11StationTxbytes"),
        ("MDS-IF-IEEE80211-MIB", "mIfDot11StationTxpackets"),
        ("MDS-IF-IEEE80211-MIB", "mIfDot11StationTxfailed"),
        ("MDS-IF-IEEE80211-MIB", "mIfDot11StationTxretries"))
)
if mibBuilder.loadTexts:
    mIfDot11StatusStationGroup.setStatus("current")

mIfDot11StatusApGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 3, 2, 3)
)
mIfDot11StatusApGroup.setObjects(
      *(("MDS-IF-IEEE80211-MIB", "mIfDot11ApSsid"),
        ("MDS-IF-IEEE80211-MIB", "mIfDot11ApClientMac"),
        ("MDS-IF-IEEE80211-MIB", "mIfDot11ApClientRssi"),
        ("MDS-IF-IEEE80211-MIB", "mIfDot11ApClientAuthenticated"),
        ("MDS-IF-IEEE80211-MIB", "mIfDot11ApClientAuthorized"),
        ("MDS-IF-IEEE80211-MIB", "mIfDot11ApClientInactive"),
        ("MDS-IF-IEEE80211-MIB", "mIfDot11ApClientRxbytes"),
        ("MDS-IF-IEEE80211-MIB", "mIfDot11ApClientRxpackets"),
        ("MDS-IF-IEEE80211-MIB", "mIfDot11ApClientTxbitrate"),
        ("MDS-IF-IEEE80211-MIB", "mIfDot11ApClientTxbytes"),
        ("MDS-IF-IEEE80211-MIB", "mIfDot11ApClientTxpackets"),
        ("MDS-IF-IEEE80211-MIB", "mIfDot11ApClientTxfailed"),
        ("MDS-IF-IEEE80211-MIB", "mIfDot11ApClientTxretries"))
)
if mibBuilder.loadTexts:
    mIfDot11StatusApGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

mIfDot11Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 3, 1, 1)
)
mIfDot11Compliance.setObjects(
      *(("MDS-IF-IEEE80211-MIB", "mIfDot11StatusCommonGroup"),
        ("MDS-IF-IEEE80211-MIB", "mIfDot11StatusStationGroup"),
        ("MDS-IF-IEEE80211-MIB", "mIfDot11StatusApGroup"))
)
if mibBuilder.loadTexts:
    mIfDot11Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MDS-IF-IEEE80211-MIB",
    **{"Byte": Byte,
       "UnsignedByte": UnsignedByte,
       "UnsignedShort": UnsignedShort,
       "Ssid": Ssid,
       "MacString": MacString,
       "mdsIfDot11MIB": mdsIfDot11MIB,
       "mIfDot11MIBObjects": mIfDot11MIBObjects,
       "mIfDot11Config": mIfDot11Config,
       "mIfDot11Status": mIfDot11Status,
       "mIfDot11StatusTable": mIfDot11StatusTable,
       "mIfDot11StatusEntry": mIfDot11StatusEntry,
       "mIfDot11SerialNumber": mIfDot11SerialNumber,
       "mIfDot11Mode": mIfDot11Mode,
       "mIfDot11TxPower": mIfDot11TxPower,
       "mIfDot11Channel": mIfDot11Channel,
       "mIfDot11StationSsid": mIfDot11StationSsid,
       "mIfDot11StationBssid": mIfDot11StationBssid,
       "mIfDot11StationRssi": mIfDot11StationRssi,
       "mIfDot11StationAuthenticated": mIfDot11StationAuthenticated,
       "mIfDot11StationAuthorized": mIfDot11StationAuthorized,
       "mIfDot11StationInactive": mIfDot11StationInactive,
       "mIfDot11StationRxbytes": mIfDot11StationRxbytes,
       "mIfDot11StationRxpackets": mIfDot11StationRxpackets,
       "mIfDot11StationTxbitrate": mIfDot11StationTxbitrate,
       "mIfDot11StationTxbytes": mIfDot11StationTxbytes,
       "mIfDot11StationTxpackets": mIfDot11StationTxpackets,
       "mIfDot11StationTxfailed": mIfDot11StationTxfailed,
       "mIfDot11StationTxretries": mIfDot11StationTxretries,
       "mIfDot11ModemType": mIfDot11ModemType,
       "mIfDot11StatusApTable": mIfDot11StatusApTable,
       "mIfDot11StatusApEntry": mIfDot11StatusApEntry,
       "mIfDot11ApSsid": mIfDot11ApSsid,
       "mIfDot11StatusApClientTable": mIfDot11StatusApClientTable,
       "mIfDot11StatusApClientEntry": mIfDot11StatusApClientEntry,
       "mIfDot11ApClientMac": mIfDot11ApClientMac,
       "mIfDot11ApClientRssi": mIfDot11ApClientRssi,
       "mIfDot11ApClientAuthenticated": mIfDot11ApClientAuthenticated,
       "mIfDot11ApClientAuthorized": mIfDot11ApClientAuthorized,
       "mIfDot11ApClientInactive": mIfDot11ApClientInactive,
       "mIfDot11ApClientRxbytes": mIfDot11ApClientRxbytes,
       "mIfDot11ApClientRxpackets": mIfDot11ApClientRxpackets,
       "mIfDot11ApClientTxbitrate": mIfDot11ApClientTxbitrate,
       "mIfDot11ApClientTxbytes": mIfDot11ApClientTxbytes,
       "mIfDot11ApClientTxpackets": mIfDot11ApClientTxpackets,
       "mIfDot11ApClientTxfailed": mIfDot11ApClientTxfailed,
       "mIfDot11ApClientTxretries": mIfDot11ApClientTxretries,
       "mdsIfDot11MIBConformance": mdsIfDot11MIBConformance,
       "mdsIfDot11MIBCompliances": mdsIfDot11MIBCompliances,
       "mIfDot11Compliance": mIfDot11Compliance,
       "mdsIfDot11MIBGroups": mdsIfDot11MIBGroups,
       "mIfDot11StatusCommonGroup": mIfDot11StatusCommonGroup,
       "mIfDot11StatusStationGroup": mIfDot11StatusStationGroup,
       "mIfDot11StatusApGroup": mIfDot11StatusApGroup}
)
