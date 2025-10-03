# SNMP MIB module (HP-SN-ROUTER-TRAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\hp\HP-SN-ROUTER-TRAP-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:51:04 2025
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

(snOspfConfigErrorType,
 snOspfExtLsdbLimit,
 snOspfIfStatusIpAddress,
 snOspfIfStatusState,
 snOspfLsdbAreaId,
 snOspfLsdbLsId,
 snOspfLsdbRouterId,
 snOspfLsdbType,
 snOspfNbrIpAddr,
 snOspfNbrRtrId,
 snOspfNbrState,
 snOspfPacketSrc,
 snOspfPacketType,
 snOspfRouterId,
 snOspfVirtIfStatusAreaID,
 snOspfVirtIfStatusNeighbor,
 snOspfVirtIfStatusState,
 snOspfVirtNbrArea,
 snOspfVirtNbrRtrId,
 snOspfVirtNbrState) = mibBuilder.importSymbols(
    "HP-SN-OSPF-GROUP-MIB",
    "snOspfConfigErrorType",
    "snOspfExtLsdbLimit",
    "snOspfIfStatusIpAddress",
    "snOspfIfStatusState",
    "snOspfLsdbAreaId",
    "snOspfLsdbLsId",
    "snOspfLsdbRouterId",
    "snOspfLsdbType",
    "snOspfNbrIpAddr",
    "snOspfNbrRtrId",
    "snOspfNbrState",
    "snOspfPacketSrc",
    "snOspfPacketType",
    "snOspfRouterId",
    "snOspfVirtIfStatusAreaID",
    "snOspfVirtIfStatusNeighbor",
    "snOspfVirtIfStatusState",
    "snOspfVirtNbrArea",
    "snOspfVirtNbrRtrId",
    "snOspfVirtNbrState")

(hp,) = mibBuilder.importSymbols(
    "HP-SN-ROOT-MIB",
    "hp")

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


# Managed Objects groups


# Notification objects

snTrapOspfIfStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 0, 3)
)
snTrapOspfIfStateChange.setObjects(
      *(("HP-SN-OSPF-GROUP-MIB", "snOspfRouterId"),
        ("HP-SN-OSPF-GROUP-MIB", "snOspfIfStatusIpAddress"),
        ("HP-SN-OSPF-GROUP-MIB", "snOspfIfStatusState"))
)
if mibBuilder.loadTexts:
    snTrapOspfIfStateChange.setStatus(
        ""
    )

snTrapOspfVirtIfStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 0, 4)
)
snTrapOspfVirtIfStateChange.setObjects(
      *(("HP-SN-OSPF-GROUP-MIB", "snOspfRouterId"),
        ("HP-SN-OSPF-GROUP-MIB", "snOspfVirtIfStatusAreaID"),
        ("HP-SN-OSPF-GROUP-MIB", "snOspfVirtIfStatusNeighbor"),
        ("HP-SN-OSPF-GROUP-MIB", "snOspfVirtIfStatusState"))
)
if mibBuilder.loadTexts:
    snTrapOspfVirtIfStateChange.setStatus(
        ""
    )

snOspfNbrStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 0, 5)
)
snOspfNbrStateChange.setObjects(
      *(("HP-SN-OSPF-GROUP-MIB", "snOspfRouterId"),
        ("HP-SN-OSPF-GROUP-MIB", "snOspfNbrIpAddr"),
        ("HP-SN-OSPF-GROUP-MIB", "snOspfNbrRtrId"),
        ("HP-SN-OSPF-GROUP-MIB", "snOspfNbrState"))
)
if mibBuilder.loadTexts:
    snOspfNbrStateChange.setStatus(
        ""
    )

snOspfVirtNbrStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 0, 6)
)
snOspfVirtNbrStateChange.setObjects(
      *(("HP-SN-OSPF-GROUP-MIB", "snOspfRouterId"),
        ("HP-SN-OSPF-GROUP-MIB", "snOspfVirtNbrArea"),
        ("HP-SN-OSPF-GROUP-MIB", "snOspfVirtNbrRtrId"),
        ("HP-SN-OSPF-GROUP-MIB", "snOspfVirtNbrState"))
)
if mibBuilder.loadTexts:
    snOspfVirtNbrStateChange.setStatus(
        ""
    )

snOspfIfConfigError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 0, 7)
)
snOspfIfConfigError.setObjects(
      *(("HP-SN-OSPF-GROUP-MIB", "snOspfRouterId"),
        ("HP-SN-OSPF-GROUP-MIB", "snOspfIfStatusIpAddress"),
        ("HP-SN-OSPF-GROUP-MIB", "snOspfPacketSrc"),
        ("HP-SN-OSPF-GROUP-MIB", "snOspfConfigErrorType"),
        ("HP-SN-OSPF-GROUP-MIB", "snOspfPacketType"))
)
if mibBuilder.loadTexts:
    snOspfIfConfigError.setStatus(
        ""
    )

snOspfVirtIfConfigError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 0, 8)
)
snOspfVirtIfConfigError.setObjects(
      *(("HP-SN-OSPF-GROUP-MIB", "snOspfRouterId"),
        ("HP-SN-OSPF-GROUP-MIB", "snOspfVirtIfStatusAreaID"),
        ("HP-SN-OSPF-GROUP-MIB", "snOspfVirtIfStatusNeighbor"),
        ("HP-SN-OSPF-GROUP-MIB", "snOspfConfigErrorType"),
        ("HP-SN-OSPF-GROUP-MIB", "snOspfPacketType"))
)
if mibBuilder.loadTexts:
    snOspfVirtIfConfigError.setStatus(
        ""
    )

snOspfIfAuthFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 0, 9)
)
snOspfIfAuthFailure.setObjects(
      *(("HP-SN-OSPF-GROUP-MIB", "snOspfRouterId"),
        ("HP-SN-OSPF-GROUP-MIB", "snOspfIfStatusIpAddress"),
        ("HP-SN-OSPF-GROUP-MIB", "snOspfPacketSrc"),
        ("HP-SN-OSPF-GROUP-MIB", "snOspfConfigErrorType"),
        ("HP-SN-OSPF-GROUP-MIB", "snOspfPacketType"))
)
if mibBuilder.loadTexts:
    snOspfIfAuthFailure.setStatus(
        ""
    )

snOspfVirtIfAuthFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 0, 10)
)
snOspfVirtIfAuthFailure.setObjects(
      *(("HP-SN-OSPF-GROUP-MIB", "snOspfRouterId"),
        ("HP-SN-OSPF-GROUP-MIB", "snOspfVirtIfStatusAreaID"),
        ("HP-SN-OSPF-GROUP-MIB", "snOspfVirtIfStatusNeighbor"),
        ("HP-SN-OSPF-GROUP-MIB", "snOspfConfigErrorType"),
        ("HP-SN-OSPF-GROUP-MIB", "snOspfPacketType"))
)
if mibBuilder.loadTexts:
    snOspfVirtIfAuthFailure.setStatus(
        ""
    )

snOspfIfRxBadPacket = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 0, 11)
)
snOspfIfRxBadPacket.setObjects(
      *(("HP-SN-OSPF-GROUP-MIB", "snOspfRouterId"),
        ("HP-SN-OSPF-GROUP-MIB", "snOspfIfStatusIpAddress"),
        ("HP-SN-OSPF-GROUP-MIB", "snOspfPacketSrc"),
        ("HP-SN-OSPF-GROUP-MIB", "snOspfPacketType"))
)
if mibBuilder.loadTexts:
    snOspfIfRxBadPacket.setStatus(
        ""
    )

snOspfVirtIfRxBadPacket = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 0, 12)
)
snOspfVirtIfRxBadPacket.setObjects(
      *(("HP-SN-OSPF-GROUP-MIB", "snOspfRouterId"),
        ("HP-SN-OSPF-GROUP-MIB", "snOspfVirtIfStatusAreaID"),
        ("HP-SN-OSPF-GROUP-MIB", "snOspfVirtIfStatusNeighbor"),
        ("HP-SN-OSPF-GROUP-MIB", "snOspfPacketType"))
)
if mibBuilder.loadTexts:
    snOspfVirtIfRxBadPacket.setStatus(
        ""
    )

snOspfTxRetransmit = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 0, 13)
)
snOspfTxRetransmit.setObjects(
      *(("HP-SN-OSPF-GROUP-MIB", "snOspfRouterId"),
        ("HP-SN-OSPF-GROUP-MIB", "snOspfIfStatusIpAddress"),
        ("HP-SN-OSPF-GROUP-MIB", "snOspfNbrRtrId"),
        ("HP-SN-OSPF-GROUP-MIB", "snOspfPacketType"),
        ("HP-SN-OSPF-GROUP-MIB", "snOspfLsdbType"),
        ("HP-SN-OSPF-GROUP-MIB", "snOspfLsdbLsId"),
        ("HP-SN-OSPF-GROUP-MIB", "snOspfLsdbRouterId"))
)
if mibBuilder.loadTexts:
    snOspfTxRetransmit.setStatus(
        ""
    )

ospfVirtIfTxRetransmit = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 0, 14)
)
ospfVirtIfTxRetransmit.setObjects(
      *(("HP-SN-OSPF-GROUP-MIB", "snOspfRouterId"),
        ("HP-SN-OSPF-GROUP-MIB", "snOspfVirtIfStatusAreaID"),
        ("HP-SN-OSPF-GROUP-MIB", "snOspfVirtIfStatusNeighbor"),
        ("HP-SN-OSPF-GROUP-MIB", "snOspfPacketType"),
        ("HP-SN-OSPF-GROUP-MIB", "snOspfLsdbType"),
        ("HP-SN-OSPF-GROUP-MIB", "snOspfLsdbLsId"),
        ("HP-SN-OSPF-GROUP-MIB", "snOspfLsdbRouterId"))
)
if mibBuilder.loadTexts:
    ospfVirtIfTxRetransmit.setStatus(
        ""
    )

snOspfOriginateLsa = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 0, 15)
)
snOspfOriginateLsa.setObjects(
      *(("HP-SN-OSPF-GROUP-MIB", "snOspfRouterId"),
        ("HP-SN-OSPF-GROUP-MIB", "snOspfLsdbAreaId"),
        ("HP-SN-OSPF-GROUP-MIB", "snOspfLsdbType"),
        ("HP-SN-OSPF-GROUP-MIB", "snOspfLsdbLsId"),
        ("HP-SN-OSPF-GROUP-MIB", "snOspfLsdbRouterId"))
)
if mibBuilder.loadTexts:
    snOspfOriginateLsa.setStatus(
        ""
    )

snOspfMaxAgeLsa = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 0, 16)
)
snOspfMaxAgeLsa.setObjects(
      *(("HP-SN-OSPF-GROUP-MIB", "snOspfRouterId"),
        ("HP-SN-OSPF-GROUP-MIB", "snOspfLsdbAreaId"),
        ("HP-SN-OSPF-GROUP-MIB", "snOspfLsdbType"),
        ("HP-SN-OSPF-GROUP-MIB", "snOspfLsdbLsId"),
        ("HP-SN-OSPF-GROUP-MIB", "snOspfLsdbRouterId"))
)
if mibBuilder.loadTexts:
    snOspfMaxAgeLsa.setStatus(
        ""
    )

snOspfLsdbOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 0, 17)
)
snOspfLsdbOverflow.setObjects(
      *(("HP-SN-OSPF-GROUP-MIB", "snOspfRouterId"),
        ("HP-SN-OSPF-GROUP-MIB", "snOspfExtLsdbLimit"))
)
if mibBuilder.loadTexts:
    snOspfLsdbOverflow.setStatus(
        ""
    )

snOspfLsdbApproachingOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 0, 18)
)
snOspfLsdbApproachingOverflow.setObjects(
      *(("HP-SN-OSPF-GROUP-MIB", "snOspfRouterId"),
        ("HP-SN-OSPF-GROUP-MIB", "snOspfExtLsdbLimit"))
)
if mibBuilder.loadTexts:
    snOspfLsdbApproachingOverflow.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-SN-ROUTER-TRAP-MIB",
    **{"snTrapOspfIfStateChange": snTrapOspfIfStateChange,
       "snTrapOspfVirtIfStateChange": snTrapOspfVirtIfStateChange,
       "snOspfNbrStateChange": snOspfNbrStateChange,
       "snOspfVirtNbrStateChange": snOspfVirtNbrStateChange,
       "snOspfIfConfigError": snOspfIfConfigError,
       "snOspfVirtIfConfigError": snOspfVirtIfConfigError,
       "snOspfIfAuthFailure": snOspfIfAuthFailure,
       "snOspfVirtIfAuthFailure": snOspfVirtIfAuthFailure,
       "snOspfIfRxBadPacket": snOspfIfRxBadPacket,
       "snOspfVirtIfRxBadPacket": snOspfVirtIfRxBadPacket,
       "snOspfTxRetransmit": snOspfTxRetransmit,
       "ospfVirtIfTxRetransmit": ospfVirtIfTxRetransmit,
       "snOspfOriginateLsa": snOspfOriginateLsa,
       "snOspfMaxAgeLsa": snOspfMaxAgeLsa,
       "snOspfLsdbOverflow": snOspfLsdbOverflow,
       "snOspfLsdbApproachingOverflow": snOspfLsdbApproachingOverflow}
)
