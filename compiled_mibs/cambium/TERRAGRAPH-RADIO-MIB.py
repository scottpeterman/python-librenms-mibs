# SNMP MIB module (TERRAGRAPH-RADIO-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\cambium\TERRAGRAPH-RADIO-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:23:38 2025
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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

tgRadioMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 60)
)
if mibBuilder.loadTexts:
    tgRadioMIB.setRevisions(
        ("2020-01-08 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class ObjectIndex(TextualConvention, Integer32):
    status = "current"
    displayHint = "x"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )



# MIB Managed Objects in the order of their OIDs

_Terragraph_ObjectIdentity = ObjectIdentity
terragraph = _Terragraph_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713)
)
_Interfaces_ObjectIdentity = ObjectIdentity
interfaces = _Interfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 60, 1)
)
_TgRadioInterfacesTable_Object = MibTable
tgRadioInterfacesTable = _TgRadioInterfacesTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 60, 1, 1)
)
if mibBuilder.loadTexts:
    tgRadioInterfacesTable.setStatus("current")
_TgRadioStatEntry_Object = MibTableRow
tgRadioStatEntry = _TgRadioStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 60, 1, 1, 1)
)
tgRadioStatEntry.setIndexNames(
    (0, "TERRAGRAPH-RADIO-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tgRadioStatEntry.setStatus("current")
_IfIndex_Type = ObjectIndex
_IfIndex_Object = MibTableColumn
ifIndex = _IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 17713, 60, 1, 1, 1, 1),
    _IfIndex_Type()
)
ifIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ifIndex.setStatus("current")
_IfName_Type = DisplayString
_IfName_Object = MibTableColumn
ifName = _IfName_Object(
    (1, 3, 6, 1, 4, 1, 17713, 60, 1, 1, 1, 2),
    _IfName_Type()
)
ifName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifName.setStatus("current")
_MacAddr_Type = DisplayString
_MacAddr_Object = MibTableColumn
macAddr = _MacAddr_Object(
    (1, 3, 6, 1, 4, 1, 17713, 60, 1, 1, 1, 3),
    _MacAddr_Type()
)
macAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macAddr.setStatus("current")
_RemoteMacAddr_Type = DisplayString
_RemoteMacAddr_Object = MibTableColumn
remoteMacAddr = _RemoteMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 17713, 60, 1, 1, 1, 4),
    _RemoteMacAddr_Type()
)
remoteMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteMacAddr.setStatus("current")
_Mcs_Type = Gauge32
_Mcs_Object = MibTableColumn
mcs = _Mcs_Object(
    (1, 3, 6, 1, 4, 1, 17713, 60, 1, 1, 1, 5),
    _Mcs_Type()
)
mcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcs.setStatus("current")
_Snr_Type = Integer32
_Snr_Object = MibTableColumn
snr = _Snr_Object(
    (1, 3, 6, 1, 4, 1, 17713, 60, 1, 1, 1, 6),
    _Snr_Type()
)
snr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snr.setStatus("current")
_Rssi_Type = Integer32
_Rssi_Object = MibTableColumn
rssi = _Rssi_Object(
    (1, 3, 6, 1, 4, 1, 17713, 60, 1, 1, 1, 7),
    _Rssi_Type()
)
rssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rssi.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TERRAGRAPH-RADIO-MIB",
    **{"ObjectIndex": ObjectIndex,
       "terragraph": terragraph,
       "tgRadioMIB": tgRadioMIB,
       "interfaces": interfaces,
       "tgRadioInterfacesTable": tgRadioInterfacesTable,
       "tgRadioStatEntry": tgRadioStatEntry,
       "ifIndex": ifIndex,
       "ifName": ifName,
       "macAddr": macAddr,
       "remoteMacAddr": remoteMacAddr,
       "mcs": mcs,
       "snr": snr,
       "rssi": rssi}
)
