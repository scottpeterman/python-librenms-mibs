# SNMP MIB module (NSCRTV-EXTENSION-GY) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\glassway\NSCRTV-EXTENSION-GY
# Produced by pysmi-1.6.2 at Thu Oct  2 11:47:45 2025
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

(sysLocation,
 sysName,
 sysObjectID,
 system) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysLocation",
    "sysName",
    "sysObjectID",
    "system")

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
 NotificationType,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _GyTrapVersion_Type(Integer32):
    """Custom type gyTrapVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("TRAPv1", 0),
          ("TRAPv2", 1))
    )


_GyTrapVersion_Type.__name__ = "Integer32"
_GyTrapVersion_Object = MibScalar
gyTrapVersion = _GyTrapVersion_Object(
    (1, 3, 6, 1, 2, 1, 1, 101),
    _GyTrapVersion_Type()
)
gyTrapVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gyTrapVersion.setStatus("mandatory")
_GyAgentStpVersion_Type = Integer32
_GyAgentStpVersion_Object = MibScalar
gyAgentStpVersion = _GyAgentStpVersion_Object(
    (1, 3, 6, 1, 2, 1, 1, 102),
    _GyAgentStpVersion_Type()
)
gyAgentStpVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gyAgentStpVersion.setStatus("mandatory")
_GyEntry_ObjectIdentity = ObjectIdentity
gyEntry = _GyEntry_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 1, 1000)
)
_GyCommon_ObjectIdentity = ObjectIdentity
gyCommon = _GyCommon_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 1, 1000, 1)
)
_GyUpdateIdentifier_Type = DisplayString
_GyUpdateIdentifier_Object = MibScalar
gyUpdateIdentifier = _GyUpdateIdentifier_Object(
    (1, 3, 6, 1, 2, 1, 1, 1000, 1, 2),
    _GyUpdateIdentifier_Type()
)
gyUpdateIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gyUpdateIdentifier.setStatus("mandatory")
_GyTrapVariables_ObjectIdentity = ObjectIdentity
gyTrapVariables = _GyTrapVariables_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 1, 1000, 1, 99)
)
_GyhbMacAddress_Type = PhysAddress
_GyhbMacAddress_Object = MibScalar
gyhbMacAddress = _GyhbMacAddress_Object(
    (1, 3, 6, 1, 2, 1, 1, 1000, 1, 99, 1),
    _GyhbMacAddress_Type()
)
gyhbMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gyhbMacAddress.setStatus("mandatory")
_GyhbIpAddress_Type = IpAddress
_GyhbIpAddress_Object = MibScalar
gyhbIpAddress = _GyhbIpAddress_Object(
    (1, 3, 6, 1, 2, 1, 1, 1000, 1, 99, 2),
    _GyhbIpAddress_Type()
)
gyhbIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gyhbIpAddress.setStatus("mandatory")
_GyhbLogicalID_Type = DisplayString
_GyhbLogicalID_Object = MibScalar
gyhbLogicalID = _GyhbLogicalID_Object(
    (1, 3, 6, 1, 2, 1, 1, 1000, 1, 99, 3),
    _GyhbLogicalID_Type()
)
gyhbLogicalID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gyhbLogicalID.setStatus("mandatory")
_GyhbModelNumber_Type = DisplayString
_GyhbModelNumber_Object = MibScalar
gyhbModelNumber = _GyhbModelNumber_Object(
    (1, 3, 6, 1, 2, 1, 1, 1000, 1, 99, 4),
    _GyhbModelNumber_Type()
)
gyhbModelNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gyhbModelNumber.setStatus("mandatory")
_GyhbSerialNumber_Type = DisplayString
_GyhbSerialNumber_Object = MibScalar
gyhbSerialNumber = _GyhbSerialNumber_Object(
    (1, 3, 6, 1, 2, 1, 1, 1000, 1, 99, 5),
    _GyhbSerialNumber_Type()
)
gyhbSerialNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gyhbSerialNumber.setStatus("mandatory")
_GyhbROCommunity_Type = DisplayString
_GyhbROCommunity_Object = MibScalar
gyhbROCommunity = _GyhbROCommunity_Object(
    (1, 3, 6, 1, 2, 1, 1, 1000, 1, 99, 6),
    _GyhbROCommunity_Type()
)
gyhbROCommunity.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gyhbROCommunity.setStatus("mandatory")
_GyhbRWCommunity_Type = DisplayString
_GyhbRWCommunity_Object = MibScalar
gyhbRWCommunity = _GyhbRWCommunity_Object(
    (1, 3, 6, 1, 2, 1, 1, 1000, 1, 99, 7),
    _GyhbRWCommunity_Type()
)
gyhbRWCommunity.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gyhbRWCommunity.setStatus("mandatory")

# Managed Objects groups


# Notification objects

gyHeartBeat = NotificationType(
    (1, 3, 6, 1, 2, 1, 1, 1000, 0, 0)
)
gyHeartBeat.setObjects(
      *(("NSCRTV-EXTENSION-GY", "gyhbMacAddress"),
        ("NSCRTV-EXTENSION-GY", "gyhbIpAddress"),
        ("NSCRTV-EXTENSION-GY", "gyhbLogicalID"),
        ("NSCRTV-EXTENSION-GY", "gyhbModelNumber"),
        ("NSCRTV-EXTENSION-GY", "gyhbSerialNumber"),
        ("NSCRTV-EXTENSION-GY", "gyhbROCommunity"),
        ("NSCRTV-EXTENSION-GY", "gyhbRWCommunity"),
        ("SNMPv2-MIB", "sysObjectID"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    gyHeartBeat.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NSCRTV-EXTENSION-GY",
    **{"gyTrapVersion": gyTrapVersion,
       "gyAgentStpVersion": gyAgentStpVersion,
       "gyEntry": gyEntry,
       "gyHeartBeat": gyHeartBeat,
       "gyCommon": gyCommon,
       "gyUpdateIdentifier": gyUpdateIdentifier,
       "gyTrapVariables": gyTrapVariables,
       "gyhbMacAddress": gyhbMacAddress,
       "gyhbIpAddress": gyhbIpAddress,
       "gyhbLogicalID": gyhbLogicalID,
       "gyhbModelNumber": gyhbModelNumber,
       "gyhbSerialNumber": gyhbSerialNumber,
       "gyhbROCommunity": gyhbROCommunity,
       "gyhbRWCommunity": gyhbRWCommunity}
)
