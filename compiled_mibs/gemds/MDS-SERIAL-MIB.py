# SNMP MIB module (MDS-SERIAL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\gemds\MDS-SERIAL-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:47:34 2025
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

(mdsServices,) = mibBuilder.importSymbols(
    "MDS-ORBIT-SMI-MIB",
    "mdsServices")

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

mdsSerialMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4130, 10, 3, 2)
)
if mibBuilder.loadTexts:
    mdsSerialMIB.setRevisions(
        ("2018-05-16 00:00",
         "2014-05-12 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MSerMIBObjects_ObjectIdentity = ObjectIdentity
mSerMIBObjects = _MSerMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4130, 10, 3, 2, 1)
)
_MSerConfig_ObjectIdentity = ObjectIdentity
mSerConfig = _MSerConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4130, 10, 3, 2, 1, 1)
)
_MSerStatus_ObjectIdentity = ObjectIdentity
mSerStatus = _MSerStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4130, 10, 3, 2, 1, 2)
)
_MSerTermServerStatusTable_Object = MibTable
mSerTermServerStatusTable = _MSerTermServerStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 3, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    mSerTermServerStatusTable.setStatus("current")
_MSerTermServerStatusEntry_Object = MibTableRow
mSerTermServerStatusEntry = _MSerTermServerStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 3, 2, 1, 2, 1, 1)
)
mSerTermServerStatusEntry.setIndexNames(
    (0, "MDS-SERIAL-MIB", "mSerTermServerSerialPort"),
)
if mibBuilder.loadTexts:
    mSerTermServerStatusEntry.setStatus("current")
_MSerTermServerSerialPort_Type = OctetString
_MSerTermServerSerialPort_Object = MibTableColumn
mSerTermServerSerialPort = _MSerTermServerSerialPort_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 3, 2, 1, 2, 1, 1, 1),
    _MSerTermServerSerialPort_Type()
)
mSerTermServerSerialPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mSerTermServerSerialPort.setStatus("current")
_MSerTermServerDescription_Type = OctetString
_MSerTermServerDescription_Object = MibTableColumn
mSerTermServerDescription = _MSerTermServerDescription_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 3, 2, 1, 2, 1, 1, 2),
    _MSerTermServerDescription_Type()
)
mSerTermServerDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mSerTermServerDescription.setStatus("current")
_MSerTermServerEnabled_Type = TruthValue
_MSerTermServerEnabled_Object = MibTableColumn
mSerTermServerEnabled = _MSerTermServerEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 3, 2, 1, 2, 1, 1, 3),
    _MSerTermServerEnabled_Type()
)
mSerTermServerEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mSerTermServerEnabled.setStatus("current")
_MSerTermServerIpTxPackets_Type = Unsigned32
_MSerTermServerIpTxPackets_Object = MibTableColumn
mSerTermServerIpTxPackets = _MSerTermServerIpTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 3, 2, 1, 2, 1, 1, 6),
    _MSerTermServerIpTxPackets_Type()
)
mSerTermServerIpTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mSerTermServerIpTxPackets.setStatus("current")
_MSerTermServerIpTxBytes_Type = Unsigned32
_MSerTermServerIpTxBytes_Object = MibTableColumn
mSerTermServerIpTxBytes = _MSerTermServerIpTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 3, 2, 1, 2, 1, 1, 7),
    _MSerTermServerIpTxBytes_Type()
)
mSerTermServerIpTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mSerTermServerIpTxBytes.setStatus("current")
_MSerTermServerIpRxPackets_Type = Unsigned32
_MSerTermServerIpRxPackets_Object = MibTableColumn
mSerTermServerIpRxPackets = _MSerTermServerIpRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 3, 2, 1, 2, 1, 1, 8),
    _MSerTermServerIpRxPackets_Type()
)
mSerTermServerIpRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mSerTermServerIpRxPackets.setStatus("current")
_MSerTermServerIpRxBytes_Type = Unsigned32
_MSerTermServerIpRxBytes_Object = MibTableColumn
mSerTermServerIpRxBytes = _MSerTermServerIpRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 3, 2, 1, 2, 1, 1, 9),
    _MSerTermServerIpRxBytes_Type()
)
mSerTermServerIpRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mSerTermServerIpRxBytes.setStatus("current")
_MSerTermServerSerialTxPackets_Type = Unsigned32
_MSerTermServerSerialTxPackets_Object = MibTableColumn
mSerTermServerSerialTxPackets = _MSerTermServerSerialTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 3, 2, 1, 2, 1, 1, 10),
    _MSerTermServerSerialTxPackets_Type()
)
mSerTermServerSerialTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mSerTermServerSerialTxPackets.setStatus("current")
_MSerTermServerSerialTxBytes_Type = Unsigned32
_MSerTermServerSerialTxBytes_Object = MibTableColumn
mSerTermServerSerialTxBytes = _MSerTermServerSerialTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 3, 2, 1, 2, 1, 1, 11),
    _MSerTermServerSerialTxBytes_Type()
)
mSerTermServerSerialTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mSerTermServerSerialTxBytes.setStatus("current")
_MSerTermServerSerialRxPackets_Type = Unsigned32
_MSerTermServerSerialRxPackets_Object = MibTableColumn
mSerTermServerSerialRxPackets = _MSerTermServerSerialRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 3, 2, 1, 2, 1, 1, 12),
    _MSerTermServerSerialRxPackets_Type()
)
mSerTermServerSerialRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mSerTermServerSerialRxPackets.setStatus("current")
_MSerTermServerSerialRxBytes_Type = Unsigned32
_MSerTermServerSerialRxBytes_Object = MibTableColumn
mSerTermServerSerialRxBytes = _MSerTermServerSerialRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 3, 2, 1, 2, 1, 1, 13),
    _MSerTermServerSerialRxBytes_Type()
)
mSerTermServerSerialRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mSerTermServerSerialRxBytes.setStatus("current")
_MdsSerMIBConformance_ObjectIdentity = ObjectIdentity
mdsSerMIBConformance = _MdsSerMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4130, 10, 3, 2, 3)
)
_MdsSerMIBCompliances_ObjectIdentity = ObjectIdentity
mdsSerMIBCompliances = _MdsSerMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4130, 10, 3, 2, 3, 1)
)
_MdsSerMIBGroups_ObjectIdentity = ObjectIdentity
mdsSerMIBGroups = _MdsSerMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4130, 10, 3, 2, 3, 2)
)

# Managed Objects groups

mSerStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4130, 10, 3, 2, 3, 2, 1)
)
mSerStatusGroup.setObjects(
      *(("MDS-SERIAL-MIB", "mSerTermServerSerialPort"),
        ("MDS-SERIAL-MIB", "mSerTermServerDescription"),
        ("MDS-SERIAL-MIB", "mSerTermServerEnabled"),
        ("MDS-SERIAL-MIB", "mSerTermServerIpTxPackets"),
        ("MDS-SERIAL-MIB", "mSerTermServerIpTxBytes"),
        ("MDS-SERIAL-MIB", "mSerTermServerIpRxPackets"),
        ("MDS-SERIAL-MIB", "mSerTermServerIpRxBytes"),
        ("MDS-SERIAL-MIB", "mSerTermServerSerialTxPackets"),
        ("MDS-SERIAL-MIB", "mSerTermServerSerialTxBytes"),
        ("MDS-SERIAL-MIB", "mSerTermServerSerialRxPackets"),
        ("MDS-SERIAL-MIB", "mSerTermServerSerialRxBytes"))
)
if mibBuilder.loadTexts:
    mSerStatusGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

mSerCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4130, 10, 3, 2, 3, 1, 1)
)
mSerCompliance.setObjects(
    ("MDS-SERIAL-MIB", "mSerStatusGroup")
)
if mibBuilder.loadTexts:
    mSerCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MDS-SERIAL-MIB",
    **{"mdsSerialMIB": mdsSerialMIB,
       "mSerMIBObjects": mSerMIBObjects,
       "mSerConfig": mSerConfig,
       "mSerStatus": mSerStatus,
       "mSerTermServerStatusTable": mSerTermServerStatusTable,
       "mSerTermServerStatusEntry": mSerTermServerStatusEntry,
       "mSerTermServerSerialPort": mSerTermServerSerialPort,
       "mSerTermServerDescription": mSerTermServerDescription,
       "mSerTermServerEnabled": mSerTermServerEnabled,
       "mSerTermServerIpTxPackets": mSerTermServerIpTxPackets,
       "mSerTermServerIpTxBytes": mSerTermServerIpTxBytes,
       "mSerTermServerIpRxPackets": mSerTermServerIpRxPackets,
       "mSerTermServerIpRxBytes": mSerTermServerIpRxBytes,
       "mSerTermServerSerialTxPackets": mSerTermServerSerialTxPackets,
       "mSerTermServerSerialTxBytes": mSerTermServerSerialTxBytes,
       "mSerTermServerSerialRxPackets": mSerTermServerSerialRxPackets,
       "mSerTermServerSerialRxBytes": mSerTermServerSerialRxBytes,
       "mdsSerMIBConformance": mdsSerMIBConformance,
       "mdsSerMIBCompliances": mdsSerMIBCompliances,
       "mSerCompliance": mSerCompliance,
       "mdsSerMIBGroups": mdsSerMIBGroups,
       "mSerStatusGroup": mSerStatusGroup}
)
