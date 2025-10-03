# SNMP MIB module (SL-RADIUS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\packetlight\SL-RADIUS-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:20:02 2025
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

(slMain,) = mibBuilder.importSymbols(
    "SL-MAIN-MIB",
    "slMain")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

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

slRadiusMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 23)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class SharedSecret(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



# MIB Managed Objects in the order of their OIDs

_SlRadiusClientMIBObjects_ObjectIdentity = ObjectIdentity
slRadiusClientMIBObjects = _SlRadiusClientMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 23, 1)
)
_SlRadiusClient_ObjectIdentity = ObjectIdentity
slRadiusClient = _SlRadiusClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 23, 1, 1)
)
_SlRadiusEnabled_Type = TruthValue
_SlRadiusEnabled_Object = MibScalar
slRadiusEnabled = _SlRadiusEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 23, 1, 1, 1),
    _SlRadiusEnabled_Type()
)
slRadiusEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slRadiusEnabled.setStatus("current")
_SlRadiusServerTable_Object = MibTable
slRadiusServerTable = _SlRadiusServerTable_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 23, 1, 1, 2)
)
if mibBuilder.loadTexts:
    slRadiusServerTable.setStatus("current")
_SlRadiusServerEntry_Object = MibTableRow
slRadiusServerEntry = _SlRadiusServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 23, 1, 1, 2, 1)
)
slRadiusServerEntry.setIndexNames(
    (0, "SL-RADIUS-MIB", "slRadiusServerIndex"),
)
if mibBuilder.loadTexts:
    slRadiusServerEntry.setStatus("current")
_SlRadiusServerIndex_Type = Integer32
_SlRadiusServerIndex_Object = MibTableColumn
slRadiusServerIndex = _SlRadiusServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 23, 1, 1, 2, 1, 1),
    _SlRadiusServerIndex_Type()
)
slRadiusServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slRadiusServerIndex.setStatus("current")
_SlRadiusServerAddress_Type = IpAddress
_SlRadiusServerAddress_Object = MibTableColumn
slRadiusServerAddress = _SlRadiusServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 23, 1, 1, 2, 1, 2),
    _SlRadiusServerAddress_Type()
)
slRadiusServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slRadiusServerAddress.setStatus("current")
_SlRadiusServerPort_Type = Integer32
_SlRadiusServerPort_Object = MibTableColumn
slRadiusServerPort = _SlRadiusServerPort_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 23, 1, 1, 2, 1, 3),
    _SlRadiusServerPort_Type()
)
slRadiusServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slRadiusServerPort.setStatus("current")


class _SlRadiusServerAdminStatus_Type(Integer32):
    """Custom type slRadiusServerAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_SlRadiusServerAdminStatus_Type.__name__ = "Integer32"
_SlRadiusServerAdminStatus_Object = MibTableColumn
slRadiusServerAdminStatus = _SlRadiusServerAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 23, 1, 1, 2, 1, 4),
    _SlRadiusServerAdminStatus_Type()
)
slRadiusServerAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slRadiusServerAdminStatus.setStatus("current")
_SlRadiusTimeout_Type = Integer32
_SlRadiusTimeout_Object = MibTableColumn
slRadiusTimeout = _SlRadiusTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 23, 1, 1, 2, 1, 5),
    _SlRadiusTimeout_Type()
)
slRadiusTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slRadiusTimeout.setStatus("current")
_SlRadiusSharedSecret_Type = SharedSecret
_SlRadiusSharedSecret_Object = MibTableColumn
slRadiusSharedSecret = _SlRadiusSharedSecret_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 23, 1, 1, 2, 1, 6),
    _SlRadiusSharedSecret_Type()
)
slRadiusSharedSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slRadiusSharedSecret.setStatus("current")
_SlRadiusTraps_ObjectIdentity = ObjectIdentity
slRadiusTraps = _SlRadiusTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 23, 1, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SL-RADIUS-MIB",
    **{"SharedSecret": SharedSecret,
       "slRadiusMIB": slRadiusMIB,
       "slRadiusClientMIBObjects": slRadiusClientMIBObjects,
       "slRadiusClient": slRadiusClient,
       "slRadiusEnabled": slRadiusEnabled,
       "slRadiusServerTable": slRadiusServerTable,
       "slRadiusServerEntry": slRadiusServerEntry,
       "slRadiusServerIndex": slRadiusServerIndex,
       "slRadiusServerAddress": slRadiusServerAddress,
       "slRadiusServerPort": slRadiusServerPort,
       "slRadiusServerAdminStatus": slRadiusServerAdminStatus,
       "slRadiusTimeout": slRadiusTimeout,
       "slRadiusSharedSecret": slRadiusSharedSecret,
       "slRadiusTraps": slRadiusTraps}
)
