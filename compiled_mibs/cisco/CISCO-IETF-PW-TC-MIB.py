# SNMP MIB module (CISCO-IETF-PW-TC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\cisco\CISCO-IETF-PW-TC-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:26:29 2025
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

(ciscoExperiment,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoExperiment")

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

cpwTCMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 20000, 1)
)
if mibBuilder.loadTexts:
    cpwTCMIB.setRevisions(
        ("2006-07-21 12:00",
         "2003-02-26 12:00",
         "2002-05-28 12:00",
         "2002-01-30 12:00",
         "2001-12-20 12:00",
         "2001-07-12 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class CpwGroupID(TextualConvention, Unsigned32):
    status = "current"


class CpwVcIDType(TextualConvention, Unsigned32):
    status = "current"


class CpwVcIndexType(TextualConvention, Unsigned32):
    status = "current"


class CpwVcVlanCfg(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4097),
    )



class CpwOperStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("testing", 3),
          ("unknown", 4),
          ("dormant", 5),
          ("notPresent", 6),
          ("lowerLayerDown", 7))
    )



class CpwVcType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("other", 0),
          ("frameRelay", 1),
          ("atmAal5Vcc", 2),
          ("atmTransparent", 3),
          ("ethernetVLAN", 4),
          ("ethernet", 5),
          ("hdlc", 6),
          ("ppp", 7),
          ("cep", 8),
          ("atmVccCell", 9),
          ("atmVpcCell", 10),
          ("ethernetVPLS", 11),
          ("e1Satop", 12),
          ("t1Satop", 13),
          ("e3Satop", 14),
          ("t3Satop", 15),
          ("basicCesPsn", 16),
          ("basicTdmIp", 17),
          ("tdmCasCesPsn", 18),
          ("tdmCasTdmIp", 19))
    )



# MIB Managed Objects in the order of their OIDs

_CpwMIB_ObjectIdentity = ObjectIdentity
cpwMIB = _CpwMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 20000)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-IETF-PW-TC-MIB",
    **{"CpwGroupID": CpwGroupID,
       "CpwVcIDType": CpwVcIDType,
       "CpwVcIndexType": CpwVcIndexType,
       "CpwVcVlanCfg": CpwVcVlanCfg,
       "CpwOperStatus": CpwOperStatus,
       "CpwVcType": CpwVcType,
       "cpwMIB": cpwMIB,
       "cpwTCMIB": cpwTCMIB}
)
