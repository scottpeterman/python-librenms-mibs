# SNMP MIB module (JUNIPER-EXPERIMENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\junos\JUNIPER-EXPERIMENT-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:06:28 2025
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

(jnxExperiment,
 juniperMIB) = mibBuilder.importSymbols(
    "JUNIPER-SMI",
    "jnxExperiment",
    "juniperMIB")

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

_JnxBgpM2Experiment_ObjectIdentity = ObjectIdentity
jnxBgpM2Experiment = _JnxBgpM2Experiment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1)
)
if mibBuilder.loadTexts:
    jnxBgpM2Experiment.setStatus("current")
_JnxLdapExperiment_ObjectIdentity = ObjectIdentity
jnxLdapExperiment = _JnxLdapExperiment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 5, 2)
)
if mibBuilder.loadTexts:
    jnxLdapExperiment.setStatus("current")
_JnxBfdExperiment_ObjectIdentity = ObjectIdentity
jnxBfdExperiment = _JnxBfdExperiment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 5, 3)
)
if mibBuilder.loadTexts:
    jnxBfdExperiment.setStatus("current")
_JnxOspfv3Experiment_ObjectIdentity = ObjectIdentity
jnxOspfv3Experiment = _JnxOspfv3Experiment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4)
)
if mibBuilder.loadTexts:
    jnxOspfv3Experiment.setStatus("current")
_JnxExampleMibRoot_ObjectIdentity = ObjectIdentity
jnxExampleMibRoot = _JnxExampleMibRoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 5, 5)
)
if mibBuilder.loadTexts:
    jnxExampleMibRoot.setStatus("current")
_JnxInternalMibRoot_ObjectIdentity = ObjectIdentity
jnxInternalMibRoot = _JnxInternalMibRoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 5, 6)
)
if mibBuilder.loadTexts:
    jnxInternalMibRoot.setStatus("current")
_JnxP2mpExperiment_ObjectIdentity = ObjectIdentity
jnxP2mpExperiment = _JnxP2mpExperiment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 5, 7)
)
if mibBuilder.loadTexts:
    jnxP2mpExperiment.setStatus("current")
_JnxL2L3VpnMcastExperiment_ObjectIdentity = ObjectIdentity
jnxL2L3VpnMcastExperiment = _JnxL2L3VpnMcastExperiment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 5, 11)
)
if mibBuilder.loadTexts:
    jnxL2L3VpnMcastExperiment.setStatus("current")
_JnxMvpnExperiment_ObjectIdentity = ObjectIdentity
jnxMvpnExperiment = _JnxMvpnExperiment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 5, 12)
)
if mibBuilder.loadTexts:
    jnxMvpnExperiment.setStatus("current")
_JnxMldpExperiment_ObjectIdentity = ObjectIdentity
jnxMldpExperiment = _JnxMldpExperiment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 5, 13)
)
if mibBuilder.loadTexts:
    jnxMldpExperiment.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-EXPERIMENT-MIB",
    **{"jnxBgpM2Experiment": jnxBgpM2Experiment,
       "jnxLdapExperiment": jnxLdapExperiment,
       "jnxBfdExperiment": jnxBfdExperiment,
       "jnxOspfv3Experiment": jnxOspfv3Experiment,
       "jnxExampleMibRoot": jnxExampleMibRoot,
       "jnxInternalMibRoot": jnxInternalMibRoot,
       "jnxP2mpExperiment": jnxP2mpExperiment,
       "jnxL2L3VpnMcastExperiment": jnxL2L3VpnMcastExperiment,
       "jnxMvpnExperiment": jnxMvpnExperiment,
       "jnxMldpExperiment": jnxMldpExperiment}
)
