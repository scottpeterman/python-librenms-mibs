# SNMP MIB module (ALCATEL-IND1-SNMP-AGENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\nokia\ALCATEL-IND1-SNMP-AGENT-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:14:18 2025
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

(softentIND1SnmpAgt,) = mibBuilder.importSymbols(
    "ALCATEL-IND1-BASE",
    "softentIND1SnmpAgt")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

alcatelIND1SNMPAgentMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1SNMPAgentMIB.setRevisions(
        ("2007-04-03 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class SnmpAgtSecurityLevel(TextualConvention, Integer32):
    status = "current"
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
        *(("noSec", 1),
          ("authSet", 2),
          ("authAll", 3),
          ("privSet", 4),
          ("privAll", 5),
          ("trapOnly", 6))
    )



# MIB Managed Objects in the order of their OIDs

_AlcatelIND1SNMPAgentMIBObjects_ObjectIdentity = ObjectIdentity
alcatelIND1SNMPAgentMIBObjects = _AlcatelIND1SNMPAgentMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1SNMPAgentMIBObjects.setStatus("current")
_SnmpAgtConfig_ObjectIdentity = ObjectIdentity
snmpAgtConfig = _SnmpAgtConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 1, 1, 1, 1)
)


class _SnmpAgtSecurityLevel_Type(SnmpAgtSecurityLevel):
    """Custom type snmpAgtSecurityLevel based on SnmpAgtSecurityLevel"""
    defaultValue = 1


_SnmpAgtSecurityLevel_Type.__name__ = "SnmpAgtSecurityLevel"
_SnmpAgtSecurityLevel_Object = MibScalar
snmpAgtSecurityLevel = _SnmpAgtSecurityLevel_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 1, 1, 1, 1, 1),
    _SnmpAgtSecurityLevel_Type()
)
snmpAgtSecurityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpAgtSecurityLevel.setStatus("current")


class _SnmpAgtCommunityMode_Type(Integer32):
    """Custom type snmpAgtCommunityMode based on Integer32"""
    defaultValue = 1

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


_SnmpAgtCommunityMode_Type.__name__ = "Integer32"
_SnmpAgtCommunityMode_Object = MibScalar
snmpAgtCommunityMode = _SnmpAgtCommunityMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 1, 1, 1, 1, 2),
    _SnmpAgtCommunityMode_Type()
)
snmpAgtCommunityMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpAgtCommunityMode.setStatus("current")
_SnmpAgtCtlFiles_ObjectIdentity = ObjectIdentity
snmpAgtCtlFiles = _SnmpAgtCtlFiles_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 1, 1, 1, 3)
)
if mibBuilder.loadTexts:
    snmpAgtCtlFiles.setStatus("current")


class _SnmpAgtSourceIpConfig_Type(Integer32):
    """Custom type snmpAgtSourceIpConfig based on Integer32"""
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
        *(("default", 1),
          ("noLoopback0", 2),
          ("ipInterface", 3))
    )


_SnmpAgtSourceIpConfig_Type.__name__ = "Integer32"
_SnmpAgtSourceIpConfig_Object = MibScalar
snmpAgtSourceIpConfig = _SnmpAgtSourceIpConfig_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 1, 1, 1, 4),
    _SnmpAgtSourceIpConfig_Type()
)
snmpAgtSourceIpConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpAgtSourceIpConfig.setStatus("obsolete")
_SnmpAgtSourceIp_Type = IpAddress
_SnmpAgtSourceIp_Object = MibScalar
snmpAgtSourceIp = _SnmpAgtSourceIp_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 1, 1, 1, 5),
    _SnmpAgtSourceIp_Type()
)
snmpAgtSourceIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpAgtSourceIp.setStatus("obsolete")
_AlcatelIND1SNMPAgentMIBConformance_ObjectIdentity = ObjectIdentity
alcatelIND1SNMPAgentMIBConformance = _AlcatelIND1SNMPAgentMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1SNMPAgentMIBConformance.setStatus("current")
_AlcatelIND1SNMPAgentMIBGroups_ObjectIdentity = ObjectIdentity
alcatelIND1SNMPAgentMIBGroups = _AlcatelIND1SNMPAgentMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1SNMPAgentMIBGroups.setStatus("current")
_AlcatelIND1SNMPAgentMIBCompliances_ObjectIdentity = ObjectIdentity
alcatelIND1SNMPAgentMIBCompliances = _AlcatelIND1SNMPAgentMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1SNMPAgentMIBCompliances.setStatus("current")

# Managed Objects groups

snmpAgtConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 1, 1, 2, 1, 1)
)
snmpAgtConfigGroup.setObjects(
      *(("ALCATEL-IND1-SNMP-AGENT-MIB", "snmpAgtSecurityLevel"),
        ("ALCATEL-IND1-SNMP-AGENT-MIB", "snmpAgtCommunityMode"))
)
if mibBuilder.loadTexts:
    snmpAgtConfigGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

alcatelIND1SNMPAgentMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 1, 1, 2, 2, 1)
)
alcatelIND1SNMPAgentMIBCompliance.setObjects(
    ("ALCATEL-IND1-SNMP-AGENT-MIB", "snmpAgtConfigGroup")
)
if mibBuilder.loadTexts:
    alcatelIND1SNMPAgentMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-SNMP-AGENT-MIB",
    **{"SnmpAgtSecurityLevel": SnmpAgtSecurityLevel,
       "alcatelIND1SNMPAgentMIB": alcatelIND1SNMPAgentMIB,
       "alcatelIND1SNMPAgentMIBObjects": alcatelIND1SNMPAgentMIBObjects,
       "snmpAgtConfig": snmpAgtConfig,
       "snmpAgtSecurityLevel": snmpAgtSecurityLevel,
       "snmpAgtCommunityMode": snmpAgtCommunityMode,
       "snmpAgtCtlFiles": snmpAgtCtlFiles,
       "snmpAgtSourceIpConfig": snmpAgtSourceIpConfig,
       "snmpAgtSourceIp": snmpAgtSourceIp,
       "alcatelIND1SNMPAgentMIBConformance": alcatelIND1SNMPAgentMIBConformance,
       "alcatelIND1SNMPAgentMIBGroups": alcatelIND1SNMPAgentMIBGroups,
       "snmpAgtConfigGroup": snmpAgtConfigGroup,
       "alcatelIND1SNMPAgentMIBCompliances": alcatelIND1SNMPAgentMIBCompliances,
       "alcatelIND1SNMPAgentMIBCompliance": alcatelIND1SNMPAgentMIBCompliance}
)
