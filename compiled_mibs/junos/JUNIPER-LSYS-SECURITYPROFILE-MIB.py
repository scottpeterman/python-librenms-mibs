# SNMP MIB module (JUNIPER-LSYS-SECURITYPROFILE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\junos\JUNIPER-LSYS-SECURITYPROFILE-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:03:41 2025
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

(jnxLsysSecurityProfile,) = mibBuilder.importSymbols(
    "JUNIPER-JS-SMI",
    "jnxLsysSecurityProfile")

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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JnxLsysSpZone_ObjectIdentity = ObjectIdentity
jnxLsysSpZone = _JnxLsysSpZone_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 1)
)
_JnxLsysSpScheduler_ObjectIdentity = ObjectIdentity
jnxLsysSpScheduler = _JnxLsysSpScheduler_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 2)
)
_JnxLsysSpPolicy_ObjectIdentity = ObjectIdentity
jnxLsysSpPolicy = _JnxLsysSpPolicy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 3)
)
_JnxLsysSpPolicywcnt_ObjectIdentity = ObjectIdentity
jnxLsysSpPolicywcnt = _JnxLsysSpPolicywcnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 4)
)
_JnxLsysSpFlowgate_ObjectIdentity = ObjectIdentity
jnxLsysSpFlowgate = _JnxLsysSpFlowgate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 5)
)
_JnxLsysSpFlowsess_ObjectIdentity = ObjectIdentity
jnxLsysSpFlowsess = _JnxLsysSpFlowsess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 6)
)
_JnxLsysSpAuthentry_ObjectIdentity = ObjectIdentity
jnxLsysSpAuthentry = _JnxLsysSpAuthentry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 7)
)
_JnxLsysSpNATsrcpool_ObjectIdentity = ObjectIdentity
jnxLsysSpNATsrcpool = _JnxLsysSpNATsrcpool_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 8)
)
_JnxLsysSpNATdstpool_ObjectIdentity = ObjectIdentity
jnxLsysSpNATdstpool = _JnxLsysSpNATdstpool_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 9)
)
_JnxLsysSpNATsrcpatad_ObjectIdentity = ObjectIdentity
jnxLsysSpNATsrcpatad = _JnxLsysSpNATsrcpatad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 10)
)
_JnxLsysSpNATsrcnopatad_ObjectIdentity = ObjectIdentity
jnxLsysSpNATsrcnopatad = _JnxLsysSpNATsrcnopatad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 11)
)
_JnxLsysSpNATsrcrule_ObjectIdentity = ObjectIdentity
jnxLsysSpNATsrcrule = _JnxLsysSpNATsrcrule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 12)
)
_JnxLsysSpNATdstrule_ObjectIdentity = ObjectIdentity
jnxLsysSpNATdstrule = _JnxLsysSpNATdstrule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 13)
)
_JnxLsysSpNATstaticrule_ObjectIdentity = ObjectIdentity
jnxLsysSpNATstaticrule = _JnxLsysSpNATstaticrule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 14)
)
_JnxLsysSpNATconebind_ObjectIdentity = ObjectIdentity
jnxLsysSpNATconebind = _JnxLsysSpNATconebind_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 15)
)
_JnxLsysSpNATpoipnum_ObjectIdentity = ObjectIdentity
jnxLsysSpNATpoipnum = _JnxLsysSpNATpoipnum_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 16)
)
_JnxLsysSpNATRuleRefPfx_ObjectIdentity = ObjectIdentity
jnxLsysSpNATRuleRefPfx = _JnxLsysSpNATRuleRefPfx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 17)
)
_JnxLsysSpCPU_ObjectIdentity = ObjectIdentity
jnxLsysSpCPU = _JnxLsysSpCPU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 18)
)
_JnxSp_ObjectIdentity = ObjectIdentity
jnxSp = _JnxSp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 19)
)
_JnxLsysSpSecurewire_ObjectIdentity = ObjectIdentity
jnxLsysSpSecurewire = _JnxLsysSpSecurewire_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 20)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-LSYS-SECURITYPROFILE-MIB",
    **{"jnxLsysSpZone": jnxLsysSpZone,
       "jnxLsysSpScheduler": jnxLsysSpScheduler,
       "jnxLsysSpPolicy": jnxLsysSpPolicy,
       "jnxLsysSpPolicywcnt": jnxLsysSpPolicywcnt,
       "jnxLsysSpFlowgate": jnxLsysSpFlowgate,
       "jnxLsysSpFlowsess": jnxLsysSpFlowsess,
       "jnxLsysSpAuthentry": jnxLsysSpAuthentry,
       "jnxLsysSpNATsrcpool": jnxLsysSpNATsrcpool,
       "jnxLsysSpNATdstpool": jnxLsysSpNATdstpool,
       "jnxLsysSpNATsrcpatad": jnxLsysSpNATsrcpatad,
       "jnxLsysSpNATsrcnopatad": jnxLsysSpNATsrcnopatad,
       "jnxLsysSpNATsrcrule": jnxLsysSpNATsrcrule,
       "jnxLsysSpNATdstrule": jnxLsysSpNATdstrule,
       "jnxLsysSpNATstaticrule": jnxLsysSpNATstaticrule,
       "jnxLsysSpNATconebind": jnxLsysSpNATconebind,
       "jnxLsysSpNATpoipnum": jnxLsysSpNATpoipnum,
       "jnxLsysSpNATRuleRefPfx": jnxLsysSpNATRuleRefPfx,
       "jnxLsysSpCPU": jnxLsysSpCPU,
       "jnxSp": jnxSp,
       "jnxLsysSpSecurewire": jnxLsysSpSecurewire}
)
