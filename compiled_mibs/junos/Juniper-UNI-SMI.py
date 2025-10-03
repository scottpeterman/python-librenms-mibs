# SNMP MIB module (Juniper-UNI-SMI) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\juniper\Juniper-UNI-SMI
# Produced by pysmi-1.6.2 at Thu Oct  2 12:03:18 2025
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

juniperUni = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874)
)
if mibBuilder.loadTexts:
    juniperUni.setRevisions(
        ("2003-07-30 19:03",
         "2002-11-13 20:14",
         "2001-06-01 21:46",
         "2000-06-01 14:30",
         "2000-05-24 04:00",
         "1999-12-13 19:36",
         "1999-11-08 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JuniProducts_ObjectIdentity = ObjectIdentity
juniProducts = _JuniProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 1)
)
_JuniperUniMibs_ObjectIdentity = ObjectIdentity
juniperUniMibs = _JuniperUniMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2)
)
if mibBuilder.loadTexts:
    juniperUniMibs.setStatus("current")
_UsVoiceMibs_ObjectIdentity = ObjectIdentity
usVoiceMibs = _UsVoiceMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 1)
)
_JuniMibs_ObjectIdentity = ObjectIdentity
juniMibs = _JuniMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2)
)
_JuniperUniExperiment_ObjectIdentity = ObjectIdentity
juniperUniExperiment = _JuniperUniExperiment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 3)
)
if mibBuilder.loadTexts:
    juniperUniExperiment.setStatus("current")
_UsVoiceExperiment_ObjectIdentity = ObjectIdentity
usVoiceExperiment = _UsVoiceExperiment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 3, 1)
)
_JuniExperiment_ObjectIdentity = ObjectIdentity
juniExperiment = _JuniExperiment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2)
)
_JuniperUniAdmin_ObjectIdentity = ObjectIdentity
juniperUniAdmin = _JuniperUniAdmin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4)
)
if mibBuilder.loadTexts:
    juniperUniAdmin.setStatus("current")
_UsVoiceAdmin_ObjectIdentity = ObjectIdentity
usVoiceAdmin = _UsVoiceAdmin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 1)
)
_JuniAdmin_ObjectIdentity = ObjectIdentity
juniAdmin = _JuniAdmin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2)
)
_JuniAgentCapability_ObjectIdentity = ObjectIdentity
juniAgentCapability = _JuniAgentCapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5)
)
if mibBuilder.loadTexts:
    juniAgentCapability.setStatus("current")
_UsVoiceAgents_ObjectIdentity = ObjectIdentity
usVoiceAgents = _UsVoiceAgents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 1)
)
_JuniAgents_ObjectIdentity = ObjectIdentity
juniAgents = _JuniAgents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2)
)
_JuniNetMgmtProducts_ObjectIdentity = ObjectIdentity
juniNetMgmtProducts = _JuniNetMgmtProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 6)
)
if mibBuilder.loadTexts:
    juniNetMgmtProducts.setStatus("current")
_JuniSdxMibs_ObjectIdentity = ObjectIdentity
juniSdxMibs = _JuniSdxMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 6, 1)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Juniper-UNI-SMI",
    **{"juniperUni": juniperUni,
       "juniProducts": juniProducts,
       "juniperUniMibs": juniperUniMibs,
       "usVoiceMibs": usVoiceMibs,
       "juniMibs": juniMibs,
       "juniperUniExperiment": juniperUniExperiment,
       "usVoiceExperiment": usVoiceExperiment,
       "juniExperiment": juniExperiment,
       "juniperUniAdmin": juniperUniAdmin,
       "usVoiceAdmin": usVoiceAdmin,
       "juniAdmin": juniAdmin,
       "juniAgentCapability": juniAgentCapability,
       "usVoiceAgents": usVoiceAgents,
       "juniAgents": juniAgents,
       "juniNetMgmtProducts": juniNetMgmtProducts,
       "juniSdxMibs": juniSdxMibs}
)
